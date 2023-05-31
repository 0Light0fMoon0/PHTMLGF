from django.db import models

# Create your models here.


#Class Player.
class Player(models.Model):
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    creds = models.IntegerField()

    posx = models.FloatField()
    posy = models.FloatField()
    place = models.CharField(max_length=50)
    
    imgup = models.CharField(max_length=50)
    imgdown = models.CharField(max_length=50)
    imgright = models.CharField(max_length=50)
    imgleft = models.CharField(max_length=50)
    animup = models.CharField(max_length=50)
    animdown = models.CharField(max_length=50)
    animleft = models.CharField(max_length=50)
    animright = models.CharField(max_length=50)
    texture = models.CharField(max_length=50)
    def __str__(self):
        return "Player %s" %self.nickname


#Class Place
class Place(models.Model):
    place = models.CharField(max_length=50)
    texture = models.CharField(max_length=50)
    txtExt = models.CharField(max_length=50)
    log = models.CharField(max_length=1000)
    owner = models.CharField(max_length=50)
    posx = models.FloatField()
    posy = models.FloatField()
    location = models.CharField(max_length=50)
    def __str__(self):
        return "Place %s" %self.place

#Class Portal
class Portal(models.Model):
    portal = models.CharField(max_length=50)
    texture = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    posx = models.FloatField()
    posy = models.FloatField()
    toPosx = models.FloatField()
    toPosy = models.FloatField()
    toPlace = models.CharField(max_length=50)
    extSize = models.FloatField()
    place = models.CharField(max_length=50)
    def __str__(self):
        return "Portal %s" %self.portal


#Class Water.
class Water(models.Model):
    water = models.CharField(max_length=50)
    texture = models.CharField(max_length=50)
    posx = models.FloatField()
    posy = models.FloatField()
    place = models.CharField(max_length=50)
    def __str__(self):
        return "Water %s" %self.water


    
#Class Decoration.
class Decoration(models.Model):
    decoration = models.CharField(max_length=50)
    texture = models.CharField(max_length=50)
    posx = models.IntegerField()
    posy = models.IntegerField()
    place = models.CharField(max_length=50)
    def __str__(self):
        return "Decoration %s" %self.decoration



