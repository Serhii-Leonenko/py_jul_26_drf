from django.urls import path
from messenger.views import message_list

app_name = "messenger"

urlpatterns = [
    path("messages/", message_list, name="message-list"),
]
