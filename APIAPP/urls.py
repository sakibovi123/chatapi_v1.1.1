from django.urls import path, include
from .views import *

urlpatterns = [
    path("users/", AllAvailableUsers.as_view()),
    # Get User Details and create a room
    path("user/<int:pk>/", GetUserIdCreateRoom.as_view()),
    # Get WelcomeMsg Room Id

    path("welcome-room/<int:pk>/", WelcomeMsgId.as_view()),

    # Get Chatroom Details and recents chats

    path("chatroom/<int:pk>/", PrivateRoomId.as_view()),

    # Send Message URl

    path("send-message/<int:pk>/", SendMessage.as_view()),
]