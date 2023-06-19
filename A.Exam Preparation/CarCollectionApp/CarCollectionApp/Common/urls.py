from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('catalogue/', views.catalogue, name="catalogue"),
]
