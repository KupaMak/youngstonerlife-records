from core.models import *


# Create your models here.
class UserAuth(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=40)
    stage_name = models.CharField(max_length=40)
    picture = models.ImageField(null=True, blank=True, upload_to='user-profile')
    code_number = models.IntegerField()


class MyNotification(models.Model):
    title = models.CharField(max_length=10)
    message = models.CharField(max_length=100)
    to = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    read = models.CharField(max_length=10)


class MyPayroll(models.Model):
    title = models.CharField(max_length=10)
    message = models.CharField(max_length=100)
    to = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    read = models.CharField(max_length=10)


class MyStudioSession(models.Model):
    title = models.CharField(max_length=10)
    message = models.CharField(max_length=100)
    to = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    read = models.CharField(max_length=10)
