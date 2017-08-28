from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from produit.models import Produit, Commercant


def group_based_upload_to_seconder(instance, filename):
    return 'image/media/ali/secondaire/' + str(instance.date) + filename


@python_2_unicode_compatible
class Message(models.Model):
    user = models.ForeignKey(User, related_name='+')
    message = models.TextField(max_length=1000, blank=True,null=True)
    objet = models.TextField(max_length=1000, blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(User, related_name='+')
    from_user = models.ForeignKey(User, related_name='+')
    is_read = models.BooleanField(default=False)
    produit = models.ForeignKey(Produit,null=True,blank=True)
    image = models.ImageField(upload_to=group_based_upload_to_seconder,null=True)
    url = models.TextField(max_length=1000, blank=True,null=True)
    commercant = models.ForeignKey(Commercant,null=True,blank=True)
    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
        ordering = ('date',)
        db_table = 'messages_message'

    def __str__(self):
        return self.message

    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    @staticmethod
    def send_message(from_user, to_user,message, image,objet,url,produit):

        current_user_message = Message(from_user=from_user,
                                       message=message,
                                       image=image,
                                       objet=objet,
                                       url=url,
                                       produit=produit,
                                       user=from_user,
                                       conversation=to_user,
                                       is_read=True)
        current_user_message.save()
        Message(from_user=from_user,
                conversation=from_user,
                message=message,
                objet=objet,
                url=url,
                image=image,
                produit=produit,
                user=to_user).save()

        return current_user_message

    @staticmethod
    def send_image_message(from_user, to_user, message=None, image=None):

        current_user_message1 = Message(from_user=from_user,
                                       message=message,
                                       image=image,
                                       user=from_user,
                                       conversation=to_user,
                                       is_read=True)
        current_user_message1.save()
        Message(from_user=from_user,
                conversation=from_user,
                message=message,
                image=image,
                user=to_user).save()

        return current_user_message1

    @staticmethod
    def send_param_message(from_user, to_user, message):

        current_user_message2 = Message(from_user=from_user,
                                        message=message,
                                        user=from_user,
                                        conversation=to_user,
                                        is_read=True)
        current_user_message2.save()
        Message(from_user=from_user,
                conversation=from_user,
                message=message,
                user=to_user).save()

        return current_user_message2

    @staticmethod
    def get_conversations(user):
        conversations = Message.objects.filter(
            user=user).values('conversation').annotate(
                last=Max('date')).order_by('-last')
        users = []
        for conversation in conversations:
            users.append({
                'user': User.objects.get(pk=conversation['conversation']),
                'last': conversation['last'],
                'unread': Message.objects.filter(user=user,
                                                 conversation__pk=conversation[
                                                    'conversation'],
                                                 is_read=False).count(),
                })


        return users



