from django.urls import path
from django.contrib import admin
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("chat_app.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/register/", include("dj_rest_auth.registration.urls")),
]
