from django.urls import path

from DevsInfo.Developers import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('hi', views.some)
]
