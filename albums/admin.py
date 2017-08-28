# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from albums.models import Album, Image

admin.site.register(Album)
admin.site.register(Image)
