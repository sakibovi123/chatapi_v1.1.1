from django.core.checks import messages
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Q
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import string
import random
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class AllAvailableUsers(APIView):
    def get(self, request, *args, **kwargs):
        all_users = User.objects.all()

        user_serializer = UserSerializer(all_users, many=True)

        return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)


class GetUserIdCreateRoom(APIView):
    def get_object(self, pk, *args, **kwargs):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk,*args, **kwargs):
        getuserId = self.get_object(pk)

        userId_serializer = UserSerializer(getuserId)

        return Response(userId_serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request, pk, *args, **kwargs):
        userId = self.get_object(pk)
        s = 10
        chat_slug = "".join(random.choices(string.ascii_uppercase + string.digits, k = s))
        sender = request.user
        receiver = userId
        query_data = request.data

        WelcomeMsgRoom.objects.create(
            chat_slug=chat_slug,
            sender=sender,
            receiver=receiver,
            welcome_msg = query_data["welcome_msg"]
        )

        return Response(status=status.HTTP_201_CREATED)



class WelcomeMsgId(APIView):
    def get_object(self, pk, *args, **kwargs):
        try:
            return WelcomeMsgRoom.objects.get(pk=pk)
        except WelcomeMsgRoom.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk, *args, **kwargs):
        welcomeId = self.get_object(pk)
        welcome_serializer = WelcomeMsgSerializer(welcomeId)
        return Response(welcome_serializer.data, status=status.HTTP_200_OK)


class PrivateRoomId(APIView):
    def get_id(self, pk, *args, **kwargs):
        try:
            return ChatRoom.objects.get(pk=pk)
        except ChatRoom.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk, *args, **kwargs):
        chatroomId = self.get_id(pk)
        chatroom_serializer = ChatRoomSerializer(chatroomId)
        return Response(chatroom_serializer.data)



# Send MEssage

class SendMessage(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def get_roomId(self, pk):
        try:
            return WelcomeMsgRoom.objects.get(pk=pk)
        except ChatRoom.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, pk, *args, **kwargs):
        roomId = self.get_roomId(pk)
        user = request.user
        qry = request.data

        ChatRoom.objects.create(
            room=roomId,
            user = user,
            message = qry["message"]
        )

        return Response(status=status.HTTP_200_OK)



# Get Message By users and rooms

class GetMessageByUser(APIView):
    def get_object(self, pk):
        return WelcomeMsgRoom.objects.get(pk=pk)
    

    def get(self, request, pk):
        get_messageId = self.get_object(pk)
        serializer = ChatRoomSerializer(get_messageId)
        return Response(serializer.data)


    def get(self, pk, *args, **kwargs):
        room = self.get_object(pk)
        message = ChatRoom.objects.filter(Q(user=room.sender) & Q(user=room.receiver))

        message_serializer = ChatRoomSerializer(message)
        return Response(message_serializer.data, status=status.HTTP_200_OK)


## Deleting Room

class DeleteWelcomeMsgRoom(APIView):
    def get_object(self, pk, *args, **kwargs):
        try:
            return WelcomeMsgRoom.objects.get(pk=pk)
        except WelcomeMsgRoom.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, pk, *args, **kwargs):
        roomId = self.get_object(pk)
        roomId.delete()

        return Response(status=status.HTTP_200_OK)


class DeleteMessage(APIView):
    def get_object(self, pk, *args, **kwargs):
        try:
            return ChatRoom.objects.get(pk=pk)
        except ChatRoom.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, pk, *args, **kwargs):
        msgId = self.get_object(pk)
        msgId.delete()

        # msgId.save()

        return Response(status=status.HTTP_200_OK)

    


