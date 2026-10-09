from rest_framework import viewsets

from messenger.models import Message, Tag
from messenger.serializers import MessageSerializer, TagSerializer, MessageListSerializer, MessageDetailSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_serializer_class(self):
        match self.action:
            case "list":
                return MessageListSerializer
            case "retrieve":
                return MessageDetailSerializer
            case _:
                return MessageSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
