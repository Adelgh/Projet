
    # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from produit.models import Boutique


def group_based_upload_to_album(instance, filename):
    return "image/media/{}/{}".format(instance.name, filename)
def group_based_upload_to_Image(instance, filename):
    return "image/media/{}/photos/{}".format(instance.album.name, filename)
class Album(models.Model):
    user = models.ForeignKey(User,default='1')
    name = models.CharField(max_length=250,null=True)
    album = models.ImageField(upload_to=group_based_upload_to_album , blank=True)
    boutique = models.ForeignKey(Boutique,on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Image(models.Model):
    user = models.ForeignKey(User,default='1')
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=group_based_upload_to_Image , blank=True)
    def __str__(self):
        return self.logo.url




