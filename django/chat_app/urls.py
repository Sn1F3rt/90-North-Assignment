from django.urls import path
from django.views.generic.base import RedirectView

from .views import *

urlpatterns = [
    path("home/", home, name="home"),
    path("", RedirectView.as_view(url="/home")),
    path("add_friend/", add_friend, name="add_friend"),
    path("friend_list/", friend_list, name="friend_list"),
    path("chat/<str:room_name>/", start_chat, name="start_chat"),
]
