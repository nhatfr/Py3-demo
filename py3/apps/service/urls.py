from django.conf.urls import include, url
from py3.apps.service.appmodels.service_list import CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
