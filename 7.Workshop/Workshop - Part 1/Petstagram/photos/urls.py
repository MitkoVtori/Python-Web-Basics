from django.urls import path

from Petstagram.photos import views


urlpatterns = [
    path('add/', views.add_photo, name='add_photo'),
    path('<int:pk>/', views.photo_details),
    path('<int:pk>/edit/', views.edit_photo),
]