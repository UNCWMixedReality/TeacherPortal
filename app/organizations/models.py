from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=128)
    org_id = models.ForeignKey(Organization, blank=True, on_delete=models.CASCADE)
    staff_id = models.ForeignKey("users.Staff", blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Headset(models.Model):
    org_id = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, blank=True, null=True)
    device_nickname = models.CharField(max_length=128, null=True, blank=True)
    device_id = models.CharField(max_length=128, default="UNREGISTERED_HEADSET", null=False, blank=False, unique=True)

    def __str__(self):
        if self.device_nickname is None:
            return self.device_id
        else:
            return self.device_nickname


class Student(models.Model):
    name = models.CharField(max_length=128)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Group(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    headset_id = models.ForeignKey(Headset, on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.course_id} : Group {self.id}"
