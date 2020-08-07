from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from flowers.models import Flower


class Action(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    flower = models.ForeignKey(
        to=Flower, on_delete=models.CASCADE, related_name='actions')
    liked = models.BooleanField(null=True)

    class Meta:
        unique_together = ['user', 'flower']
