from django.contrib import admin

from .models import Comment, ContactMessage, Like, Post, PostView


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at", "views_count", "likes_count", "comments_count")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_at")
    search_fields = ("body",)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_at")


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ("post", "session_key", "viewed_at")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    readonly_fields = ("created_at",)
