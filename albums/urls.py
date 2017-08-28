from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^album/(?P<boutique_id>[0-9]+)$', views.album, name='album'),

url(r'^(?P<album_id>[0-9]+)/image/$', views.image, name='image'),
url(r'^all_album/$', views.all_album,name='all_album'),
url(r'^(?P<boutique_id>[0-9]+)/album_detail/$', views.detail_album, name='detail_album'),

]