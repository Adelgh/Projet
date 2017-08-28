from django.forms import ModelForm
from wishlist.models import WishCollection


class WishCollectionForm(ModelForm):
  class Meta:
    model = WishCollection
    fields = ['name']