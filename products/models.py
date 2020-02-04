from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=235)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name

