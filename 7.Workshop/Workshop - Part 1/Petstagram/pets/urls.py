from django.urls import path

from Petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet, name='add_pet'),
    path('<str:username>/pet/<slug:pet_name>/', views.show_details_page),
    path('<str:username>/pet/<slug:pet_name>/edit/', views.edit_page),
    path('<str:username>/pet/<slug:pet_name>/delete/', views.delete_pet),
]