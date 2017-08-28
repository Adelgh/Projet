import os
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from ajax_select import urls as ajax_select_urls
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^messages/', include('messenger.urls')),
    url(r'^api/creation/', include('produit.api.urls', namespace='creation-api')),
    url(r'^api/msg/', include('messenger.api.urls', namespace='list-msg')),
    url(r'^api/list_react/', include('reaction.api.urls', namespace='list-api')),

    url(r'^post/', include('post.urls')),
    url(r'^boutique/', include('produit.urls')),
    url(r'^', include('produit.urls')),
    url(r'^auth/', include('authentication.urls')),

    url(r'^', include('notification.urls')),
    url(r'^', include('reaction.urls')),
    url(r'^ajax_select/', include(ajax_select_urls)),
    url(r'^', include('albums.urls')),
    url(r'^wishlist/', include('wishlist.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'image'))

