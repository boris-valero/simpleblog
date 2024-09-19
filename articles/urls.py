from django.urls import path
from django.conf.urls import include, url

from .views import detail

app_name = 'articles'
urlpatterns = [
    path(r'<slug:slug>-<int:id>/', detail, name='detail'),
]