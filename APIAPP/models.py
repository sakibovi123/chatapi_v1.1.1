from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid


class CustomUser(models.Model):
    joined_at = models.DateTimeField(default=datetime.now)
    username = models.CharField(max_length=255, unique=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to="images/")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "CustomUser"
        ordering = ["-id"]

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.password1 != self.password2:
            return 404
        else:
            super(CustomUser, self).save(*args, **kwargs)


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.token

    def save(self, *args, **kwargs):
        super(Token, self).save(*args, **kwargs)


class WelcomeMsgRoom(models.Model):
    chat_slug = models.SlugField()
    created_at = models.DateTimeField(default=datetime.now)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    welcome_msg = models.TextField()

    class Meta:
        verbose_name_plural = "WelcomeMsgRoom"
        ordering = ["-id"]
        unique_together = ["sender", "receiver"]

    def __str__(self):
        return str(self.id)


class ChatRoom(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    room = models.ForeignKey(WelcomeMsgRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "ChatRoom"
        ordering = ["-id"]

    def __str__(self):
        return str(self.room)