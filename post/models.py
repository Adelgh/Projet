from __future__ import unicode_literals

import os
from django.contrib.auth.models import User
from django.db import models
from django.contrib.staticfiles.templatetags.staticfiles import static

from website import settings


def group_based_upload_to_categori(instance, filename):
    return "image/media/{}".format(filename)

def group_based_upload_to_categorie(instance, filename):
    return "image/media/categorie/{}".format(filename)


class Categorie(models.Model):
    name = models.TextField(null=True,max_length=50)
    logo = models.ImageField(upload_to=group_based_upload_to_categorie,blank=True,null=True)

    def __str__(self):
        return self.logo.url


class Post(models.Model):
    user = models.ForeignKey(User, default=1)
    categorie = models.ForeignKey(Categorie,blank=False,null=True,default='2')
    image = models.ImageField(upload_to=group_based_upload_to_categori,blank=True,default=None)
    post = models.TextField(blank=True,null=True,max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    class Meta :
        ordering = ('-date',)

    def get_likes_count(self):
        return self.post_reaction_set.filter(type='like').count()

    def get_dislikes_count(self):
        return self.post_reaction_set.filter(type='dislike').count()

class Commentaire(models.Model):
    user = models.ForeignKey(User, default=1)
    post = models.ForeignKey(Post,null=True,blank=True)
    text = models.CharField(null=True,max_length=1500)
    date = models.DateTimeField(auto_now_add=True)

    def get_comment_count(self):
        return self.commentaire_reaction_set.filter(type='comment').count()