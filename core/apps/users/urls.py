from django.urls import path
from django.contrib.auth import views as auth_views
from core.apps.users import views

urlpatterns = [
    path("signup/", views.CustomUserCreateView.as_view(), name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("<int:user_id>/", views.profile, name="profile"),
]
