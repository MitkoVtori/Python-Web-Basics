from django.urls import path
from FruitipediaApp.Fruit import views


urlpatterns = [
    path('details/', views.fruit_details, name='fruit details'),
    path('edit/', views.edit_fruit, name='edit fruit'),
    path('delete/', views.delete_fruit, name='delete fruit')
]
