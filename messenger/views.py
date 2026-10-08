from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from messenger.models import Message
from messenger.serializers import MessageSerializer


@api_view(["GET", "POST"])
def message_list(request: Request) -> Response:
    if request.method == "GET":
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = MessageSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
