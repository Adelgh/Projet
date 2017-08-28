from django.forms import ModelForm
from models import Post, Categorie, Commentaire


class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = ['categorie','post', 'image']


class CategorieForm(ModelForm):
  class Meta :
    model = Categorie
    fields = ['name','logo']


class CommentaireForm(ModelForm) :
  class Meta :
    model = Commentaire
    fields = ['text']