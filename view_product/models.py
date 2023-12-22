# models.py
from django.db import models
from account.models import CustomUser

class UserInfo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)
    cookie = models.CharField( max_length=200, null=True, blank=True)
    session_id = models.CharField( max_length=200, null=True, blank=True)
    os = models.CharField( max_length=200, null=True, blank=True)
    name = models.CharField( max_length=200, null=True, blank=True)
    computer_name = models.CharField(max_length=200, null=True, blank=True)
    user_agent = models.CharField( max_length=200, null=True, blank=True)
    ip_address = models.CharField( max_length=200, null=True, blank=True)
    referrer = models.CharField( max_length=200, null=True, blank=True)

class UserAction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"

class Vistor(models.Model):
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True)
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE,  null=True, blank=True)
