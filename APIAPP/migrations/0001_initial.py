# Generated by Django 3.2.9 on 2021-11-22 07:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateTimeField(default=datetime.datetime.now)),
                ('username', models.CharField(max_length=255, unique=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password1', models.CharField(max_length=255)),
                ('password2', models.CharField(max_length=255)),
                ('profile_picture', models.ImageField(upload_to='images/')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'CustomUser',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='WelcomeMsgRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_slug', models.SlugField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('welcome_msg', models.TextField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='APIAPP.customuser')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='APIAPP.customuser')),
            ],
            options={
                'verbose_name_plural': 'WelcomeMsgRoom',
                'ordering': ['-id'],
                'unique_together': {('sender', 'receiver')},
            },
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIAPP.welcomemsgroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIAPP.customuser')),
            ],
            options={
                'verbose_name_plural': 'ChatRoom',
                'ordering': ['-id'],
            },
        ),
    ]
