# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from albums.forms import ALbumForm, ImageForm
from albums.models import Album, Image
from produit.models import Boutique


def album(request,boutique_id) :
    albums = Album.objects.filter(user = request.user)
    boutique = get_object_or_404(Boutique,pk = boutique_id)
    if request.method == 'POST':

        form = ALbumForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.boutique = boutique
            obj.save()
            return render(request ,'album/detail_album.html' ,{'albums' : albums})
    form = ALbumForm()
    if  request.user.username :
        return render(request, 'album/cree_album.html', {'form': form , 'albums' : albums })



def image(request,album_id) :
    album = get_object_or_404(Album, pk=album_id)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.album = album
            obj.user = request.user
            obj.save()
            return render(request,'album/detail_album.html',{'album' : album, 'image' : obj })
    images = Image.objects.filter(album__id = album_id)
    form = ImageForm()
    return render(request, 'album/ImageForm.html', {'images': images ,'form': form , 'album' : album  })

def all_album(request) :
    albums = Album.objects.all()
    return render(request, 'album/all_albums.html', { 'album' : albums  })


def detail_album(request,boutique_id) :
    user = request.user
    boutique = get_object_or_404(Boutique, pk=boutique_id)
    image = Image.objects.filter(album__boutique_id = boutique_id)
    album = Album.objects.all()
    return render(request, 'album/detail_album.html', {'images' : image ,'album' : album, 'boutique':boutique, 'user': user})
