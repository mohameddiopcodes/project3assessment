from django.db import models
from django.urls import reverse

# Create your models here.
class Wish(models.Model):
    item = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse("wish_list")
    