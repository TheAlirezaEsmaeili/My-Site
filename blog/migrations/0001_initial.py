import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="عنوان")),
                ("slug", models.SlugField(allow_unicode=True, blank=True, max_length=220, unique=True, verbose_name="اسلاگ")),
                ("summary", models.CharField(blank=True, max_length=300, verbose_name="خلاصه")),
                ("content", models.TextField(verbose_name="متن کامل")),
                ("cover_image", models.ImageField(blank=True, null=True, upload_to="posts/", verbose_name="تصویر شاخص")),
                ("published_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="تاریخ انتشار")),
                ("author", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="posts", to=settings.AUTH_USER_MODEL, verbose_name="نویسنده")),
            ],
            options={
                "verbose_name": "پست",
                "verbose_name_plural": "پست‌ها",
                "ordering": ["-published_at"],
            },
        ),
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120, verbose_name="نام")),
                ("email", models.EmailField(max_length=254, verbose_name="ایمیل")),
                ("message", models.TextField(verbose_name="پیام")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "پیام تماس",
                "verbose_name_plural": "پیام‌های تماس",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("post", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="likes", to="blog.post")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="likes", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "لایک",
                "verbose_name_plural": "لایک‌ها",
                "unique_together": {("post", "user")},
            },
        ),
        migrations.CreateModel(
            name="PostView",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("session_key", models.CharField(max_length=40)),
                ("viewed_at", models.DateTimeField(auto_now_add=True)),
                ("post", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="post_views", to="blog.post")),
            ],
            options={
                "verbose_name": "بازدید",
                "verbose_name_plural": "بازدیدها",
                "unique_together": {("post", "session_key")},
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("body", models.TextField(max_length=1000, verbose_name="متن کامنت")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")),
                ("post", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="blog.post", verbose_name="پست")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="comments", to=settings.AUTH_USER_MODEL, verbose_name="کاربر")),
            ],
            options={
                "verbose_name": "کامنت",
                "verbose_name_plural": "کامنت‌ها",
                "ordering": ["-created_at"],
            },
        ),
    ]
