from django.db import models
from account.models import Account

class Notification(models.Model):
    text = models.TextField()
    for_user = models.ForeignKey(Account, on_delete=models.CASCADE)
    unread = models.BooleanField(default=True)
