from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_car, name="create car"),
    path('<int:car_id>/details/', views.car_details, name="car details"),
    path('<int:car_id>/edit/', views.car_edit, name="car edit"),
    path('<int:car_id>/delete/', views.delete_car, name="delete car")
]
