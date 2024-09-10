from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from core.apps.posts.services import PostService


def get_post(request, post_id):
    post_service = PostService()
    post_entity = post_service.get(post_id)

    return render(request, "posts/post_detail.html", {"post": post_entity})


def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        user_id = request.user.id

        if title and content:
            post_service = PostService()
            post_entity = post_service.create(
                title=title,
                content=content,
                user_id=user_id,
            )
            return HttpResponseRedirect(reverse("get_post", args=[post_entity.id]))

    return render(request, "posts/create_post.html")


def get_posts_by_user(request):
    user_id = request.user.id

    post_service = PostService()
    posts = post_service.get_posts_by_user(user_id)

    return render(request, "posts/posts_by_user.html", {"posts": posts})
