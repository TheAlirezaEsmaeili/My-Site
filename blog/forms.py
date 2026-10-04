from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comment, ContactMessage


class RegisterForm(UserCreationForm):
    """فرم ثبت‌نام کاربر با ایمیل."""

    email = forms.EmailField(required=True, label="ایمیل")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "username": "نام کاربری",
            "email": "you@example.com",
            "password1": "رمز عبور",
            "password2": "تکرار رمز عبور",
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": placeholders.get(field_name, ""),
            })


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "نظر خود را بنویسید...",
                "rows": 3,
            })
        }
        labels = {"body": ""}


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "نام و نام خانوادگی"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "you@example.com"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "پیام شما...", "rows": 5}),
        }
        labels = {"name": "نام", "email": "ایمیل", "message": "پیام"}
