from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from post import views

urlpatterns = [

    url(r'^post/$', views.post, name='post'),
    url(r'^categorie/$', views.categorie, name='categorie'),
    url(r'^all_posts/$', views.all_posts, name='all_posts'),
    url(r'^Acceuil/$', views.Acceuil, name='Acceuil'),
    url(r'^user_posts/(?P<post_id>[0-9]+)/$',views.user_posts , name='user_posts'),
    url(r'^user_post/(?P<username>[^/]+)/$', views.user_post, name='user_post'),

    url(r'^comment/(?P<post_id'r'>[0-9]+)$', views.comment, name='comment'),
    url(r'^$', views.categoriefilter, name='categoriefilter'),

]