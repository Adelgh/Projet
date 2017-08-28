from django.forms import ModelForm
from models import Album, Image


class ALbumForm(ModelForm):
  class Meta:
    model = Album
    fields = ['name', 'album']

class ImageForm(ModelForm) :
  class Meta:
    model = Image
    fields = ['logo']

