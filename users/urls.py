from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile_view

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile_view, name="profile")
]