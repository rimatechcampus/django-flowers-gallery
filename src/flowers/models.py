from django.db import models

# Create your models here.


class Flower(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    description = models.TextField(max_length=2000)
    description_ar = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
