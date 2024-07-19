from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from entity.serializers.serializer import NotificationSerializer


class ScheduleNotificationView(APIView):

    @staticmethod
    def post(request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
