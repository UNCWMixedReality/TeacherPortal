from django.contrib import admin

from .models import Course, Organization

# Register your models here.

admin.site.register(Organization, admin.ModelAdmin)
admin.site.register(Course, admin.ModelAdmin)
