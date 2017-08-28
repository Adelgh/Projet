# coding=utf-8
from __future__ import unicode_literals
import datetime
from django.contrib.auth.models import User
from django.db import models


def group_based_upload_to(instance, filename):
    return "image/media/{}/{}/{}".format(instance.user,instance.name, filename)


class Boutique(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, default=1)
    logo = models.ImageField(upload_to=group_based_upload_to)
    users_list = models.ManyToManyField(User,related_name='user')
    message_param = models.TextField(default='welcome to my boutique')

    def __str__(self):
        return self.name


class Commercant(models.Model):
    status_professionel = models.CharField(max_length=250)
    lien_fb = models.CharField(max_length=1000)
    user = models.ForeignKey(User, default=1)
    def __str__(self):
        return self.user

now = datetime.datetime.now()
def group_based_upload_to_produit(instance, filename):
    return "image/media/{}/{}/{}/pricipale/{}".format(instance.boutique.user,instance.boutique.name,instance.title, filename)
def group_based_upload_to_secondere(instance, filename):
    return 'image/media/{}/{}/{}/' + str(instance) + filename


def group_based_upload_to_seconder(instance, filename):
    return "image/media/{}/{}/{}/secondaire/{}".format(instance.boutique.user,instance.boutique.name,instance.title, filename)





class Image(models.Model):
    image1 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)
    image2 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)
    image3 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)





class Produit(models.Model):
    user = models.ForeignKey(User, default=1)
    choix_categorie = (('bijoux', 'bijoux'), ('maison et ameublement', 'maison et ameublement'), ('vetements', 'vetements'),('art et collections', 'art et collections'),('accessoires', 'accessoires'),('sacs et bagages', 'sacs et bagages'),('mariage', 'mariage'),)
    prix = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    etat = models.BooleanField(default=False)
    descreption = models.CharField(max_length=250,null = True)
    boutique = models.ForeignKey(Boutique,null=True, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=group_based_upload_to_produit)
    image1 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)
    image2 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)
    image3 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)
    categorie = models.CharField(max_length=250, choices=choix_categorie, default="bijoux")
    date = models.DateTimeField(auto_now_add = True , null = True)
    tags = models.CharField(max_length=250 , null=True)
    gender = (('homme','homme'),('femme','femme'))
    genre = models.CharField(max_length=250 ,null=True, choices=gender)
    genrecat = (('bébé','bébé'),('enfant','enfant'),('adulte','adulte'))
    genrt = models.CharField(null= True , max_length=250 , choices=genrecat)
    wishcollection = models.ManyToManyField('wishlist.WishCollection')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)



class wish(models.Model):
    name = models.CharField(max_length=250)
    wishlist = models.ManyToManyField(Produit, related_name='produit')
    user = models.ForeignKey(User , default='1')

    def __str__(self):
        return self.name








