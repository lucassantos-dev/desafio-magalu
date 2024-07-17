from django.contrib import admin

from .models import Status, Channel, Notification

# Register your models here.

admin.site.register(Status)
admin.site.register(Channel)
admin.site.register(Notification)
