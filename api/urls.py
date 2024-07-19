from django.urls import path
from .views import ScheduleNotificationView


urlpatterns = [
    path('schedule_notification/', ScheduleNotificationView.as_view(), name='schedule_notification'),
]
