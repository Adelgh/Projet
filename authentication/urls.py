from django.conf.urls import url
from authentication import views

urlpatterns=[
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^account/edit/$', views.edit_user_view, name='edit_user_profile'),
    url(r'^(?P<username>[^/]+)/$', views.profile, name='profile'),
    url(r'^friend/invite/$', views.friend_invite,name='friend_invite'),

]