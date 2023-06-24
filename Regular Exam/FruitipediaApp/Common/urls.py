from django.urls import path
from FruitipediaApp.Common import views


urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_fruit, name='create fruit')
]
