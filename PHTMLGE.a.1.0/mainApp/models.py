from django.db import models


class Carrusel(models.Model):
    name = models.CharField(max_length=300)
    body = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    date = models.CharField(max_length=300)

    def __str__(self):
        return "Carrusel %s" %self.name

class New(models.Model):
    name = models.CharField(max_length=300)
    body = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    date = models.CharField(max_length=300)

    def __str__(self):
        return "New %s" %self.name


class Event(models.Model):
    name = models.CharField(max_length=300)
    body = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    date = models.CharField(max_length=300)

    def __str__(self):
        return "Event %s" %self.name


# Create your models here.
