from django.conf.urls import url
from . import views

urlpatterns=[

url(r'^react/(?P<pk>\d+)/$', views.react, name='react'),
url(r'^post_react/(?P<pk>\d+)/$', views.post_react, name='post_react'),

]