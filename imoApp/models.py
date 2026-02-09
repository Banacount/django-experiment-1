from django.db import models

# Create your models here.
class ImoItem(models.Model):
    user_name = models.CharField(max_length=104)
    user_opinion = models.CharField(max_length=1024)
