from django.conf.urls import url


from reaction.api.views import ReactionListAPIView, ReactionCreateAPIView

urlpatterns=[
    url(r'^list/$', ReactionListAPIView.as_view(), name='list'),
    url(r'^react/$', ReactionCreateAPIView.as_view(), name='react'),

]