from django.contrib import admin
from .models import Post, Vote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "created_at")
    readonly_fields = ("id",)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "vote_type")
    readonly_fields = ("id",)
