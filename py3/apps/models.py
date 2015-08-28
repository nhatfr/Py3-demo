from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    store = models.ForeignKey(Store)

    def __str__(self):
        return self.name
