from django.db import models


# Create your models here.
class YourGoals(models.Model):
    title = models.CharField(max_length=120)
    isDone = models.BooleanField(default=False)


# For chatting yes
class UniversalChat(models.Model):
    text = models.CharField(max_length=1080)
    text_id = models.CharField(max_length=260)
    user_name = models.CharField(max_length=100)
