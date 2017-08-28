from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Wishlist(models.Model):
    user = models.OneToOneField(User)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}'s wishlist".format(self.user.username)
        

class WishCollection(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.name


def create_user_wishlist(sender, instance, created, **kwargs):
    if created:
        Wishlist.objects.create(user=instance)

def save_user_wishlist(sender, instance,created, **kwargs):
    if created:

        instance.wishlist.save()

post_save.connect(create_user_wishlist, sender=User)
post_save.connect(save_user_wishlist, sender=User)