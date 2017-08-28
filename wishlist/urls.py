from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wishlist_view, name='wishlist'),
    url(r'^collection/new$', views.new_collection_view, name='new_collection'),
    url(r'^collection/(?P<pk>\d+)$', views.detail_collection_view, name='detail_collection'),
    url(r'^collection/(?P<pk>\d+)/delete$', views.delete_collection_view, name='delete_collection'),
    url(r'^collection/(?P<pk>\d+)/add/(?P<product_id>\d+)$', views.add_product_view, name='add_product'),
    url(r'^collection/(?P<pk>\d+)/remove/(?P<product_id>\d+)$', views.remove_product_view, name='remove_product'),
    url(r'^(?P<pk>\d+)$', views.user_wishlist_view, name='user_wishlist'),
]