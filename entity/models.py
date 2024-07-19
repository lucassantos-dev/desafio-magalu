import uuid

from django.db import models

from .enums import ChannelsEnums, StatusEnums


class Channel(models.Model):
    channel_id = models.CharField(
        max_length=8, choices=[(tag.value, tag.name) for tag in ChannelsEnums]
    )

    def __str__(self):
        return self.channel_id


class Status(models.Model):
    status_id = models.CharField(
        max_length=9, choices=[(tag.value, tag.name) for tag in StatusEnums]
    )

    def __str__(self):
        return self.status_id


class Notification(models.Model):
    notification_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    local_date_time = models.DateTimeField(null=False, blank=False)
    destination = models.CharField(max_length=255)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, null=True, blank=True)
