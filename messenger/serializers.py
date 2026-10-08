from rest_framework import serializers

from messenger.models import Message


class MessageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict) -> Message:
        return Message.objects.create(**validated_data)
