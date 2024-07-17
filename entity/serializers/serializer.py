from rest_framework import serializers

from ..models import Channel, Status, Notification


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ("channel_id",)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class NotificationSerializer(serializers.Serializer):
    class Meta:
        model = Notification
        fields = "__all__"
