from django.db import models
import string
import random
# Create your models here.


class Items(models.Model):
    item_id = models.CharField(
        max_length=5, unique=True)
    gender = models.CharField(max_length=10)
    master_category = models.CharField(max_length=20)
    sub_category = models.CharField(max_length=20)
    article_type = models.CharField(max_length=20)
    base_color = models.CharField(max_length=20)
    season = models.CharField(max_length=20)
    year = models.CharField(max_length=10)
    usage = models.CharField(max_length=20)
    display_name = models.CharField(max_length=100)
    image_path = models.CharField(max_length=500, default="")
