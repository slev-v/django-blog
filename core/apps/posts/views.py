from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from core.apps.posts.exceptions import (
    ForbiddenException,
    PostNotFoundException,
    InvalidVoteTypeException,
)
from core.apps.posts.services.posts import PostService
from core.apps.posts.services.votes import VoteService
from core.apps.posts.models import Post


def get_post(request, post_id):
    post_service = PostService()
    try:
        post_entity = post_service.get(post_id)
    except PostNotFoundException:
        raise Http404()

    return render(request, "posts/post_detail.html", {"post": post_entity})


@login_required
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


def get_latest_posts(request):
    post_service = PostService()
    posts = post_service.get_latest_posts()

    return render(request, "posts/post_feed.html", {"posts": posts})


@login_required
def vote(request, post_id, vote_type):
    if vote_type == 2:
        vote_type = -1

    user_id = request.user.id
    vote_service = VoteService()

    try:
        vote_service.vote(post_id, user_id, vote_type)
    except InvalidVoteTypeException as e:
        return render(request, "400.html", {"message": e.message}, status=400)
    except PostNotFoundException:
        raise Http404()

    next_url = request.GET.get("next", None)
    if not next_url:
        next_url = reverse("get_post", args=[post_id])

    return redirect(next_url)


@login_required
def update(request, post_id):
    post_service = PostService()
    post = get_object_or_404(Post, id=post_id)

    if post.user_id != request.user.id:
        return render(request, "403.html", status=403)

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        user_id = request.user.id

        if title and content:
            try:
                post_entity = post_service.update(
                    post_id=post_id, user_id=user_id, title=title, content=content
                )
            except ForbiddenException:
                return render(request, "403.html", status=403)
            except PostNotFoundException:
                raise Http404()
            return HttpResponseRedirect(reverse("get_post", args=[post_entity.id]))

    return render(request, "posts/update.html", {"post": post})


@login_required
def delete(request, post_id):
    user_id = request.user.id
    post_service = PostService()
    post = get_object_or_404(Post, id=post_id)

    if post.user_id != request.user.id:
        return render(request, "403.html", status=403)

    try:
        post_service.delete(post_id, user_id)
    except ForbiddenException:
        return render(request, "403.html", status=403)
    except PostNotFoundException:
        raise Http404()

    return HttpResponseRedirect(reverse("post_feed"))
