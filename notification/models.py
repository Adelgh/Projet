from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

from post.models import Post
from produit.models import Produit


class Notification(models.Model):
    NORMAL = 'normal'
    SMILE = 'smile'
    LOVE = 'love'
    WISH = 'wish'
    LIKE = 'like'
    DISLIKE = 'dislike'

    NOTIFICATION_TYPES = (
        (NORMAL, 'normal'),
        (SMILE, 'smile'),
        (LOVE, 'love'),
        (WISH, 'wish'),
        (LIKE, 'like'),
        (DISLIKE, 'dislike'),
    )

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Produit, on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=255, choices=NOTIFICATION_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    @staticmethod
    def send(from_user, to_user, product, type):
        notification = Notification(from_user=from_user,
                                    to_user=to_user,
                                    product=product,
                                    type=type).save()

        return notification
    @staticmethod

    def send_post(from_user, to_user, post, type):
        notification = Notification(from_user=from_user,
                                         to_user=to_user,
                                         post=post,
                                         type=type).save()
        return notification


