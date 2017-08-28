from django.forms import ModelForm, forms
from models import Profile


class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['picture', 'gender' , 'age']

