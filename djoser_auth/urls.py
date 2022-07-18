import djoser.urls.base
from django.urls import re_path, include, path
import django.contrib.auth

djoser_auth_urlpatterns = [
    path('/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.authtoken'))
]
