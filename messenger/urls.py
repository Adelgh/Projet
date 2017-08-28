from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.inbox, name='inbox'),
    url(r'^new/$', views.new, name='new_message'),
    url(r'^send/$', views.send, name='send_message'),
    url(r'^send1/$', views.send1, name='send_message1'),
    url(r'^delete/$', views.delete, name='delete_message'),
    url(r'^users/$', views.users, name='users_message'),
    url(r'^check/$', views.check, name='check_message'),
    url(r'^filter/$', views.filter, name='filter'),
    url(r'^latest/$', views.latest, name='latest_message'),
    url(r'^upload/$', views.upload, name='upload'),

    url(r'^(?P<username>[^/]+)/$', views.messages, name='messages'),

]