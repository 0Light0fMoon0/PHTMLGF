#Start coding.
import os
import time
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

#Classes


#Class Player.
class EntityPlayer():
    def __init__(self,nickname,password,creds,posx,posy,place,imgup,imgdown,imgleft,imgright,animup,animdown,animleft,animright,texture):
        self.nickname = nickname
        self.password = password

        self.creds = creds
        
        self.posx = posx
        self.posy = posy
        self.place = place
        self.moving = False
        
        self.imgup = imgup
        self.imgdown = imgdown
        self.imgright = imgright
        self.imgleft = imgleft
        self.animup = animup
        self.animdown = animdown
        self.animleft = animleft
        self.animright = animright
        self.texture = texture

        self.camera_x = 0
        self.camera_y = 0

    def funcShowing(self,imganim):
        self.texture = imganim
    
    def funcCollision(self,psx,psy):
        pass

    def funcCamera(self):
            self.camera_x = 50 - self.posx
            self.camera_y = 50 - self.posy

    def moveUp(self):
        if self.posy > 2.2222 and self.moving == False:
            self.moving = True
            self.posyend = self.posy - 2.2222
            while self.posy > self.posyend:
                self.funcShowing(self.animup)
                time.sleep(0.25)
                self.posy = self.posy - 0.4444
            self.posy = self.posyend
            self.funcShowing(self.animup)
            self.funcCamera()
            self.moving = False 

    def moveDown(self):
        if self.posy < 97.778 and self.moving == False:
            self.moving = True
            self.posyend = self.posy + 2.2222
            while self.posy < self.posyend:
                self.funcShowing(self.animdown)
                time.sleep(0.25)
                self.posy = self.posy + 0.4444
            self.posy = self.posyend
            self.funcShowing(self.animdown)
            self.funcCamera()
            self.moving = False 

    def moveLeft(self):
        if self.posx > 1.25 and self.moving == False:
            self.moving = True
            self.posxend = self.posx - 1.25
            while self.posx > self.posxend:
                self.funcShowing(self.animleft)
                time.sleep(0.25)
                self.posx = self.posx - 0.25
            self.posx = self.posxend
            self.funcShowing(self.animleft)
            self.funcCamera()
            self.moving = False 

    def moveRight(self):
        if self.posx < 98.75 and self.moving == False:
            self.moving = True
            self.posxend = self.posx + 1.25
            while self.posx < self.posxend:
                self.funcShowing(self.animright)
                time.sleep(0.25)
                self.posx = self.posx + 0.25
            self.posx = self.posxend
            self.funcShowing(self.animright)
            self.funcCamera()
            self.moving = False 

    def joinPlace(self,newPosx,newPosy,newPlace):
        self.place = newPlace
        self.posx = newPosx
        self.posy = newPosy



#Class Place.
class EntityPlace():
    def __init__(self,place,texture,txtExt,log,owner,posx,posy,location):
        self.place = place
        self.texture = texture
        self.txtExt = txtExt
        self.log = log
        self.owner = owner
        self.posx = posx
        self.posy = posy
        self.location = location

    def sendMessage(self,player,message):
        player=player
        message=message
        message= player.nickname + ' : ' + message + ' \n ' 
        self.log = message + self.log


#Class Portal.
class EntityPortal():
    def __init__(self,portal,texture,owner,posx,posy,toPosx,toPosy,toPlace,extSize,place):
        self.portal = portal
        self.texture = texture
        self.owner = owner
        self.posx = posx
        self.posy = posy
        self.toPosx = toPosx
        self.toPosy = toPosy
        self.toPlace = toPlace
        self.extSize = extSize
        self.place = place
        self.maxWidth = 1.25 * extSize
        self.maxHeight = 2.2222 * extSize

    def playerJoin(self,psx,psy):
        maxPosx = self.posx + self.maxWidth
        maxPosy = self.posy + self.maxHeight
        if psx >= self.posx and psx <= maxPosx:
            if psy >= self.posy and psy <= maxPosy:
                return True
            else:
                return False
        else:
            return False

#Class Water.
class EntityWater():
    def __init__(self,water,posx,posy,place):
        self.water = water
        self.texture = texture
        self.posx = posx
        self.posy = posy
        self.place = place


#Class Decoration.
class EntityDecoration():
    def __init__(self,decoration,texture,posx,posy,place):
        self.decoration = decoration
        self.texture = texture
        self.posx = posx
        self.posy = posy
        self.place = place

#Class GUI.
class EntityWindow():
    def __init__(self,nameWindow,tittle):
        self.nameWindow = nameWindow
        self.tittle = tittle 

class EntityNotification():
    def __init__(self,nameWindow,tittle,body,state):
        self.nameWindow = nameWindow
        self.tittle = tittle 
        self.body = body 
        self.state = state 


