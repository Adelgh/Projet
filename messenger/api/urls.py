from django.conf.urls import url

from messenger.api.views import MessageListAPIView, MessageCreateAPIView

urlpatterns=[
    url(r'^list_msg/$', MessageListAPIView.as_view(), name='list_msg'),
    url(r'^create_msg/$', MessageCreateAPIView.as_view(), name='create_msg'),

]