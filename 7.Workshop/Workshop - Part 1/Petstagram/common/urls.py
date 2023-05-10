from django.urls import path

from Petstagram.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
]