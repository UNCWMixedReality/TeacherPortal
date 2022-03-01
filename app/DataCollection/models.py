from django.db import models
from organizations.models import Course


# Create your models here.
class SessionData(models.Model):
    data = models.JSONField()


class ScheduledSession(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
