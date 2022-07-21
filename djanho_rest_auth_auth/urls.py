from django.urls import re_path, include, path

from djanho_rest_auth_auth.views import TestView

rest_auth_urlpatterns = [
    re_path(r'^dj-rest-auth/', include('dj_rest_auth.urls')),
    re_path(r'^dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/test/', TestView.as_view(), name='test-path')
]