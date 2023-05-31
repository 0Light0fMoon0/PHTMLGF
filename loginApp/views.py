from django.shortcuts import render, redirect
from django.http import HttpResponse
from engineApp.models import Player 
from engineApp.engineClass import *
from django.contrib import messages
from mainApp.views import pConnecteds,places,waters,decorations

#Global Vars

#Login Function.
def funcLogin(request):
    logged=False
    tittle="Python HTML Game Engine"
    player=None

    if request.session.get('logged'):
        logged = True
        messages.success(request, 'You has been logged.')
        return redirect('/engine/')
        
            
    if 'btnLogin' in request.POST:
        txtUsername=str(request.POST['txtUsername'])
        txtPassword=str(request.POST['txtPassword'])
        playerLoadeds = Player.objects.all()

        for p in playerLoadeds:

            if p.nickname == txtUsername:
                if p.password == txtPassword:
                    player = EntityPlayer(nickname=p.nickname,creds=p.creds,password=p.password,posx=p.posx,posy=p.posy,place=p.place,imgup=p.imgup,imgdown=p.imgdown,imgleft=p.imgleft,imgright=p.imgright,animup=p.animup,animdown=p.animdown,animleft=p.animleft,animright=p.animright,texture=p.texture)
                    request.session['player']=player.nickname
                    request.session['logged']=True
                    pConnecteds.append(player)
                    logged=True
                    messages.success(request, 'You has been logged.')
                    return redirect('/engine/')                       
                
    
    return render(request, 'login.html',{'tittle':tittle, 'player':player, 'logged':logged})


# Create your views here.
