from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^service_list/', include('py3.apps.service.urls'))
]
