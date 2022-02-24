from django.db import models


# Create your models here.
class SessionData(models.Model):
    data = models.JSONField()
