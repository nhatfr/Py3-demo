from django.conf.urls import include, url
from py3.apps.service.views import (
        CategoryListView, ServiceListView
)

urlpatterns = [
    url(r'^category/$',CategoryListView.as_view()),
    url(r'^category/(?P<category>.+)/$', CategoryListView.as_view() ),
    url(r'^services/$', ServiceListView.as_view()),
]
