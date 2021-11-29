from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *
import uuid
from rest_framework.authtoken.models import Token

user = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(
            user=user,
        )
        return user


class WelcomeMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeMsgRoom
        fields = "__all__"


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = "__all__"




