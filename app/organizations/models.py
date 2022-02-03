from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=128)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    staff_id = models.ForeignKey("users.Staff", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Headset(models.Model):
    org_id = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
    mac_address = models.CharField(max_length=12, null=False, blank=False)


class Student(models.Model):
    name = models.CharField(max_length=128)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)


class Group(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    headset_id = models.ForeignKey(Headset, on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(Student)
