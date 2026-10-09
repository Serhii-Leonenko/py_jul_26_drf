from rest_framework import generics, viewsets

from messenger.models import Message, Tag
from messenger.serializers import MessageSerializer, TagSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
