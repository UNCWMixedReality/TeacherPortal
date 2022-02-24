from django.contrib import admin

from .models import Course, Group, Headset, Organization, Student

# Register your models here.

admin.site.register(Organization, admin.ModelAdmin)
admin.site.register(Course, admin.ModelAdmin)
admin.site.register(Student, admin.ModelAdmin)
admin.site.register(Headset, admin.ModelAdmin)
admin.site.register(Group, admin.ModelAdmin)
