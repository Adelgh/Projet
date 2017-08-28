# Register your models here.
from django.contrib import admin

from messenger.models import Message
from notification.models import Notification
from post.models import Commentaire
from reaction.models import Post_Reaction
from .models import Boutique, Produit, Commercant, wish
from authentication.models import Profile

# Register your models here.
admin.site.register(Boutique)
admin.site.register(Commentaire)
admin.site.register(Notification)
admin.site.register(wish)

admin.site.register(Produit)
admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Commercant)


