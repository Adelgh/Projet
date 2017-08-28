from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from post.models import Post, Commentaire
from produit.models import Produit


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, blank=True, null=True, choices=(('NORMAL', 'normal'), ('SMILE', 'smile'), ('LOVE', 'love'), ('WISH', 'wish'),))
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = (('user', 'product'),)


    @staticmethod
    def get_choices():
        return [choice[1] for choice in Reaction._meta.get_field('type').choices]


class Post_Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, blank=True, null=True, choices=(('LIKE', 'like'), ('DISLIKE', 'dislike'),))
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = (('user', 'post'),)


    @staticmethod
    def get_choice():
        return [choice[1] for choice in Post_Reaction._meta.get_field('type').choices]


class Commentaire_Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Commentaire, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, blank=True, null=True, choices=(('COMMENT', 'comment'),))
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'comment'),)


    @staticmethod
    def get_choice():
        return [choice[1] for choice in Commentaire_Reaction._meta.get_field('type').choices]

