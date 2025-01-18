from django.urls import path
from django.contrib import admin
from django.urls.conf import include
from django.views.generic import TemplateView
from django_channel.views import logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/auth/", include("dj_rest_auth.urls")
    ),  # Login, logout, password reset, etc.
    path(
        "api/auth/registration/", include("dj_rest_auth.registration.urls")
    ),  # Registration
    path(
        "login/", TemplateView.as_view(template_name="auth/login.html"), name="login"
    ),
    path(
        "register/",
        TemplateView.as_view(template_name="auth/register.html"),
        name="register",
    ),
    path("logout/", logout_view, name="logout"),
    path("", include("chat_app.urls")),
]
