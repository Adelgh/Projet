from django.conf.urls import url
from . import views

app_name = 'boutique'
urlpatterns=[
    url(r'^create_boutique/$', views.create_boutique, name='create_boutique'),
    url(r'^$', views.index, name='index'),
    url(r'^produit/(?P<filter_by>[a-zA-Z]+)/$', views.produit, name='produits'),
    url(r'^(?P<boutique_id>[0-9]+)/create_produit/$', views.create_produit, name='create_produit'),
    url(r'^(?P<boutique_id>[0-9]+)/delete_produit/(?P<produit_id>[0-9]+)/$', views.delete_produit, name='delete_produit'),
    url(r'^(?P<boutique_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<boutique_id>[0-9]+)/delete_boutique/$', views.delete_boutique, name='delete_boutique'),
    url(r'^vosproduit/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail_produit'),
    url(r'^discover/$', views.post_list, name='post_list'),
    url(r'^produits/$', views.post_list2, name='post_list2'),
    url(r'^activer/(?P<produit_id>[0-9]+)/$', views.Activer, name='Activer'),
    url(r'^copy/(?P<produit_id>[0-9]+)/$', views.produit_copy, name='produit_copy'),
    url(r'^(?P<boutique_id>[0-9]+)/update/(?P<pk>[0-9]+)/$',views.ProduitUpdate.as_view(),name='produitUpdate'),
    url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^prix/$', views.prix, name='prix'),
    url(r'^blabla/$', views.produits, name='produits'),
    url(r'^(?P<boutique_id>[0-9]+)/boutique_detail/$', views.boutique_detail, name='boutique_detail'),
    url(r'^create_wishlist/$', views.create_wishlist, name='create_wishlist'),

]
