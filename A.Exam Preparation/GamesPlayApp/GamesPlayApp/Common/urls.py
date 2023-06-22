from django.urls import path
from GamesPlayApp.Common import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('dashboard/', views.dashboard, name='dashboard')
]
