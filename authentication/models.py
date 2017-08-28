import hashlib
import os
import urllib

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.staticfiles.templatetags.staticfiles import static

from django.db import models

from notification.models import Notification
from website import settings

def group_based_upload_user_picture(instance, filename):
    return "image/media/{}/{}/{}".format(instance.user.username,instance.user.date_joined, filename)
class Profile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to=group_based_upload_user_picture, null=True, blank=True)
    gender = models.TextField(max_length=10, choices=(('FEMALE', 'female'), ('MALE', 'male'),), blank=True, null=True)
    age = models.IntegerField(null=True)

    class Meta:
        db_table = 'auth_profile'

    def __str__(self):
        return self.user.username



    def get_picture(self):
        if self.picture:
            return os.path.join(settings.MEDIA_URL, self.picture.url)
        return static(os.path.join('img', 'user.png'))

    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username

    def get_all_notifications(self):
        if Notification.objects.filter(to_user=self.user).exists():
            return Notification.objects.filter(to_user=self.user)
        return None

    def get_unread_notifications(self):
        if Notification.objects.filter(to_user=self.user, is_read=False).exists():
            return Notification.objects.filter(to_user=self.user, is_read=False)
        return None

    def read_all_notifications(self):
        notifications = Notification.objects.filter(to_user=self.user, is_read=False).update(is_read=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
