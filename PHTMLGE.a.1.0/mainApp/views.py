from django.shortcuts import render, redirect
from django.http import HttpResponse
from engineApp.models import *
from engineApp.engineClass import *
from mainApp.models import Carrusel, New, Event
from django.contrib import messages

#Global Variables.
    #Chargers.
pConnecteds = []
places = []
portals = []
waters = []
decorations = []
windows = []
PlacesLoaded = Place.objects.all()
PortalsLoaded = Portal.objects.all()
WatersLoaded = Water.objects.all()
DecorationsLoaded = Decoration.objects.all()
for pl in PlacesLoaded:
    newPlace = EntityPlace(place=pl.place,texture=pl.texture,txtExt=pl.txtExt,log=pl.log,owner=pl.owner,posx=pl.posx,posy=pl.posy,location=pl.location) 
    places.append(newPlace)
for po in PortalsLoaded:
    newPortal = EntityPortal(portal=po.portal,texture=po.texture,owner=po.owner,posx=po.posx,posy=po.posy,toPosx=po.toPosx,toPosy=po.toPosy,toPlace=po.toPlace,extSize=po.extSize,place=po.place) 
    portals.append(newPortal)
for wt in WatersLoaded:
    newWater = EntityWater(water=wt.water,texture=wt.texture,posx=wt.posx,posy=wt.posy,place=wt.place) 
    waters.append(newWater)
for dc in DecorationsLoaded:
    newDecoration = EntityDecoration(decoration=dc.decoration,texture=dc.texture,posx=dc.posx,posy=dc.posy,place=dc.place) 
    decorations.append(newDecoration)
        
        #Windows Chargers. Charge your windows in memory here.
windowExample = EntityWindow(nameWindow="windowExample",tittle="Window Example")
windows.append(windowExample)
windowExample2 = EntityWindow(nameWindow="windowExample2",tittle="Window Example 2")
windows.append(windowExample2)

def funcMain(request):
    global pConnecteds
    numofplayers = 0
    numplayer = 0
    logged=False
    player=None
    if request.session.get('logged'):
        logged=True
        for p in pConnecteds:
            numofplayers = numofplayers + 1
            if str(p.nickname) == str(request.session['player']):
                player = EntityPlayer(nickname=p.nickname,creds=p.creds,password=p.password,posx=p.posx,posy=p.posy,place=p.place,imgup=p.imgup,imgdown=p.imgdown,imgleft=p.imgleft,imgright=p.imgright,animup=p.animup,animdown=p.animdown,animleft=p.animleft,animright=p.animright,texture=p.texture)
                numplayer = numofplayers

        if numplayer == 0:
            logged = False
            del request.session['player']
            del request.session['logged']
            logged = False
            messages.success(request, 'You has been logout.')
            return redirect('/')

    tittle="Python HTML Game Engine"
    carrusels = Carrusel.objects.all()
    news = New.objects.all()
    events = Event.objects.all()
    if 'btnLogout' in request.POST:
        a=0
        for p in pConnecteds:
            if str(p.nickname) == str(request.session['player']):
                del pConnecteds[a]
                del request.session['player']
                del request.session['logged']
                logged = False
                messages.success(request, 'You has been logout.')
                return redirect('/')
                break
            else:
                a=a+1

        
    if 'btnLog' in request.POST:

        return redirect('/login')

    return render(request, 'main.html',{'tittle':tittle, 'carrusels':carrusels, 'news':news, 'events':events, 'logged':logged, 'player':player,'pConnecteds':pConnecteds, 'places':places, 'waters':waters, 'decorations':decorations, 'windows':windows})

# Create your views here.
