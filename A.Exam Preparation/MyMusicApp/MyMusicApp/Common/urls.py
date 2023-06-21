from django.urls import path
from MyMusicApp.MyMusicApp.Common import views

urlpatterns = [
    path('', views.index, name='home')
]
