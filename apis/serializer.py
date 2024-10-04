from rest_framework import serializers
from .models import Data,ChatHistory, Chats
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields= ('user_id', 'email', 'name', 'password')

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model=Data
        fields=('name','description')


class ChatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatHistory
        fields = ['prompt_id', 'chat_id', 'prompt', 'answer']


class ChatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chats
        fields = ['chat_id', 'user_id', 'timestamp', 'chat_title']
