from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from .forms import CommentForm, ContactForm, RegisterForm
from .models import Like, Post, PostView

class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.all()[:3]
        return context


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "پیام شما با موفقیت ارسال شد. به‌زودی پاسخ می‌دهیم.")
        return redirect("contact")
    return render(request, "blog/contact.html", {"form": form})


def blog_list(request):
    """فهرست همه‌ی پست‌های ولاگ به صورت کارت."""
    posts = Post.objects.all()
    return render(request, "blog/blog_list.html", {"posts": posts})


def _register_view(request, post):
    """ثبت یک بازدید برای پست بر اساس نشست کاربر (بدون شمارش تکراری)."""
    if not request.session.session_key:
        request.session.create()
    PostView.objects.get_or_create(post=post, session_key=request.session.session_key)


def post_detail(request, slug):
    """نمایش کامل یک پست همراه با کامنت‌ها و فرم ثبت کامنت."""
    post = get_object_or_404(Post, slug=slug)
    _register_view(request, post)

    comment_form = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.warning(request, "برای ثبت نظر ابتدا وارد حساب کاربری خود شوید.")
            return redirect("login")
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, "نظر شما ثبت شد.")
            return redirect("post_detail", slug=post.slug)

    context = {
        "post": post,
        "comments": post.comments.select_related("user"),
        "comment_form": comment_form,
        "is_liked": post.is_liked_by(request.user),
    }
    return render(request, "blog/post_detail.html", context)


@login_required
def like_post(request, slug):
    """لایک / لغو لایک یک پست توسط کاربر واردشده."""
    post = get_object_or_404(Post, slug=slug)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect("post_detail", slug=post.slug)


class RegisterView(CreateView):
    """ثبت‌نام کاربر جدید و ورود خودکار پس از ثبت‌نام."""

    form_class = RegisterForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, "ثبت‌نام با موفقیت انجام شد. خوش آمدید!")
        return response


class VlogLoginView(LoginView):
    """صفحه‌ی ورود اختصاصی سایت."""

    template_name = "blog/login.html"
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, "نام کاربری یا رمز عبور اشتباه است.")
        return super().form_invalid(form)
