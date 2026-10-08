from rest_framework import serializers

from messenger.models import Message, Tag


class MessageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict) -> Message:
        return Message.objects.create(**validated_data)


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data: dict) -> Tag:
        return Tag.objects.create(**validated_data)
