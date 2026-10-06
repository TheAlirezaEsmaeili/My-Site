from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    """یک پست ولاگ."""

    title = models.CharField("عنوان", max_length=200)
    slug = models.SlugField("اسلاگ", max_length=220, unique=True, blank=True, allow_unicode=True)
    summary = models.CharField("خلاصه", max_length=300, blank=True)
    content = models.TextField("متن کامل")
    status = models.BooleanField(default=False)
    cover_image = models.ImageField(
        "تصویر شاخص", upload_to="posts/", blank=True, null=True
    )
    author = models.ForeignKey(
        User,
        verbose_name="نویسنده",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
    )
    published_at = models.DateTimeField("تاریخ انتشار", default=timezone.now)

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست‌ها"
        ordering = ["-published_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # ساخت خودکار اسلاگ از روی عنوان در صورت خالی بودن
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    @property
    def views_count(self):
        return self.post_views.count()

    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def comments_count(self):
        return self.comments.count()

    def is_liked_by(self, user):
        if not user.is_authenticated:
            return False
        return self.likes.filter(user=user).exists()


class Comment(models.Model):
    """کامنت کاربران روی یک پست."""

    post = models.ForeignKey(Post, verbose_name="پست", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="کاربر", on_delete=models.CASCADE, related_name="comments"
    )
    body = models.TextField("متن کامنت", max_length=1000)
    created_at = models.DateTimeField("تاریخ ثبت", auto_now_add=True)

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت‌ها"
        ordering = ["-created_at"]

    def __str__(self):
        return f"کامنت {self.user} روی {self.post}"


class Like(models.Model):
    """لایک یک کاربر برای یک پست."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک‌ها"
        unique_together = ("post", "user")

    def __str__(self):
        return f"لایک {self.user} روی {self.post}"


class PostView(models.Model):
    """ثبت بازدید یک پست (برای شمارش بازدید بدون تکرار در یک نشست)."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_views")
    session_key = models.CharField(max_length=40)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "بازدید"
        verbose_name_plural = "بازدیدها"
        unique_together = ("post", "session_key")

    def __str__(self):
        return f"بازدید از {self.post}"


class ContactMessage(models.Model):
    """پیام ارسالی از فرم ارتباط با ما."""

    name = models.CharField("نام", max_length=120)
    email = models.EmailField("ایمیل")
    message = models.TextField("پیام")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"
        ordering = ["-created_at"]

    def __str__(self):
        return f"پیام از {self.name}"
