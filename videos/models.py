from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
