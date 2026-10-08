from rest_framework import status, generics

from rest_framework.response import Response
from rest_framework.views import APIView

from messenger.models import Message, Tag
from messenger.serializers import MessageSerializer, TagSerializer


class BaseListCreateView(APIView):
    model = None
    serializer_class = None

    def get(self, request):
        messages = self.model.objects.all()
        serializer = self.serializer_class(messages, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class MessageView(BaseListCreateView):
    model = Message
    serializer_class = MessageSerializer


class TagView(BaseListCreateView):
    model = Tag
    serializer_class = TagSerializer

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class MessageView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer