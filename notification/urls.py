from django.conf.urls import url
from . import views


urlpatterns=[

    url(r'^notifications/$', views.notifications, name='notifications'),
    url(r'^notifications/check/$', views.check_notifications, name='check'),
    url(r'^notifications/count/$', views.count_notifications, name='count'),

]