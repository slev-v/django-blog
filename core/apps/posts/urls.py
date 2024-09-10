from django.urls import path
from . import views

urlpatterns = [
    path("<int:post_id>/", views.get_post, name="get_post"),
    path("create/", views.create_post, name="create_post"),
    path("my-posts/", views.get_posts_by_user, name="get_posts_by_user"),
]
