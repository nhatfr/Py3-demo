from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/demo/', include('py3.apps.service.urls'))
]
