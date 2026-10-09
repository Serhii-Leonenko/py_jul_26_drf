from django.contrib.auth import get_user_model
from rest_framework import serializers

from messenger.models import Message, Tag

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            "id",
            "text",
            "created_at",
            "user"
        )


class MessageListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", allow_null=True)

    class Meta:
        model = Message
        fields = (
            "id",
            "created_at",
            "text_preview",
            "user"
        )


class MessageDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = (
            "id",
            "created_at",
            "text_preview",
            "text",
            "user"
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")
