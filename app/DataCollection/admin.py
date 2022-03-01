from django.contrib import admin

from .models import ScheduledSession, SessionData

# Register your models here.

admin.site.register(SessionData, admin.ModelAdmin)
admin.site.register(ScheduledSession, admin.ModelAdmin)
