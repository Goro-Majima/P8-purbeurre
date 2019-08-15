from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home),
    re_path(r'^results', views.results),
    re_path(r'^mentions', views.mentions),
]