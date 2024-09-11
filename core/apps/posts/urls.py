from django.urls import path
from . import views

urlpatterns = [
    path("<int:post_id>/vote/<int:vote_type>/", views.vote, name="vote"),
    path("<int:post_id>/update/", views.update, name="update_post"),
    path("<int:post_id>/delete/", views.delete, name="delete_post"),
    path("<int:post_id>/", views.get_post, name="get_post"),
    path("create/", views.create_post, name="create_post"),
    path("feed/", views.get_latest_posts, name="post_feed"),
]
