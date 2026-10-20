from celery import shared_task

from messenger.models import Message


@shared_task
def create_random_message():
    Message.objects.create(text="Random message from celery")
