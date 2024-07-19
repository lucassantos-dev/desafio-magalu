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


class NotificationSerializer(serializers.ModelSerializer):
    channel = serializers.SlugRelatedField(slug_field='channel_id', queryset=Channel.objects.all())
    status = serializers.SlugRelatedField(slug_field='status_id', queryset=Status.objects.all())

    class Meta:
        model = Notification
        fields = "__all__"

    def create(self, validated_data):
        return Notification.objects.create(**validated_data)
