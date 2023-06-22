from django.shortcuts import render, redirect
from django.http import HttpResponse
from engineApp.models import Player, Place, Portal, Water, Decoration
from engineApp.engineClass import *
from django.contrib import messages
from mainApp.views import pConnecteds,places,portals,waters,decorations,windows,notification
import time

#Engine Function.
def funcEngine(request):
    global pConnecteds
    numofplayers = 0
    numplayer = 0
    logged=False
    player=None

#Login check.
    if request.session.get('logged'):
        logged=True
        for p in pConnecteds:
            numofplayers = numofplayers + 1
            if str(p.nickname) == str(request.session['player']):
                player = EntityPlayer(nickname=p.nickname,creds=p.creds,password=p.password,posx=p.posx,posy=p.posy,place=p.place,imgup=p.imgup,imgdown=p.imgdown,imgleft=p.imgleft,imgright=p.imgright,animup=p.animup,animdown=p.animdown,animleft=p.animleft,animright=p.animright,texture=p.texture)
                numplayer = numofplayers
                p.funcCamera()

        if numplayer == 0:
            logged = False
            del request.session['player']
            del request.session['logged']
            logged = False
            messages.success(request, 'You has been logout.')
            return redirect('/')
    else:
        return redirect('/login/')
    tittle="Python HTML Game Engine"


#Buttons.
    
    #Button Logout.
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

    #Button Login.
    if 'btnLog' in request.POST:

        return redirect('/login')

    #Checking Button.
    if request.method == 'POST':
        task = request.POST
        if 'btnUp' == task['task']:
            for p in pConnecteds:
                if p.nickname == player.nickname:
                    p.moveUp()
        if 'btnLeft' == task['task']:
            for p in pConnecteds:
                if p.nickname == player.nickname:
                    p.moveLeft()
        if 'btnDown' == task['task']:
            for p in pConnecteds:
                if p.nickname == player.nickname:
                    p.moveDown()
        if 'btnRight' == task['task']:
            for p in pConnecteds:
                if p.nickname == player.nickname:
                    p.moveRight()
        if 'btnActionA' == task['task']:
            for p in pConnecteds:
                if p.nickname == player.nickname:
#                    p.actionA(player)
                    pass
        if 'btnActionB' == task['task']:
            for p in pConnecteds:
                if p.nickname == player.nickname:
                    for po in portals:
                        if po.place == p.place:
                            compVar = po.playerJoin(p.posx,p.posy)
                            if compVar == True:
                                player.joinPlace(po.toPosx,po.toPosy,po.toPlace)
                                p.joinPlace(po.toPosx,po.toPosy,po.toPlace)
                                break

        if 'btnActionC' == task['task']:
            for p in pConnecteds:
                if p.nickname == player.nickname:
#                    p.actionB(player)
                    pass
        if 'Send' == task['task']:
            message=task['task2']
            for pl in places:
                if player.place == pl.place:
                    for p in pConnecteds:
                        if p.nickname == player.nickname:
                            if '/' not in message:
                                pl.sendMessage(p,message)
                            if message == '/getpos':
                                notification.body = 'Your position is X: ',p.posx,' Y: ',p.posy
                                notification.state = True
                                print(notification.body)
                                time.sleep(3)
                                notification.state = False

    return render(request, 'engine.html',{'tittle':tittle, 'logged':logged, 'player':player,'pConnecteds':pConnecteds, 'places':places, 'waters':waters, 'decorations':decorations, 'windows':windows, 'notification':notification})

