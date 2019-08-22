from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'), #need to display something else
    re_path(r'^results', views.results, name='results'),
    re_path(r'^mentions', views.mentions, name='mentions'),
    re_path(r'^ajax_calls/search/', views.autocompleteModel),
]