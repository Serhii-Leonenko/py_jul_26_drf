from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters import rest_framework as rest_filters
from rest_framework import filters, viewsets

from messenger.filters import MessageFilter
from messenger.models import Message, Tag
from messenger.pagination import MessagePagination
from messenger.serializers import (
    MessageCreateSerializer,
    MessageDetailSerializer,
    MessageListSerializer,
    MessageSerializer,
    TagSerializer,
)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.select_related("user")
    serializer_class = MessageSerializer
    filter_backends = [
        filters.SearchFilter,
        rest_filters.DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = ["text", "user__username"]
    filterset_class = MessageFilter
    ordering_fields = ["created_at"]
    pagination_class = MessagePagination

    def get_serializer_class(self):
        match self.action:
            case "create":
                return MessageCreateSerializer
            case "list":
                return MessageListSerializer
            case "retrieve":
                return MessageDetailSerializer
            case _:
                return MessageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@method_decorator(cache_page(60 * 15, key_prefix="tags"), name="list")
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
