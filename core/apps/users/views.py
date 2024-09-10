from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render

from core.apps.users.forms import CustomUserCreationForm
from core.apps.users.models import CustomUser
from core.apps.posts.models import Post


class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("post_feed")


def profile(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    posts = Post.objects.filter(user=user)
    context = {
        "user": user,
        "posts": posts,
    }
    return render(request, "users/profile.html", context)
