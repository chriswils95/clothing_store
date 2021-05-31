from django.db import models
import string
import random
# Create your models here.


class Items(models.Model):
    item_id = models.CharField(
        max_length=50, unique=True)
    master_category = models.CharField(max_length=20)
