from django.conf.urls import url


from produit.api.views import ProduitCreateAPIView, ProduitListAPIView

urlpatterns=[
    url(r'^create/$', ProduitCreateAPIView.as_view(), name='create'),
    url(r'^list/$', ProduitListAPIView.as_view(), name='list'),

]