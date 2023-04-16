from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('department/<int:department_id>/', views.show_department_by_id),
    path('department/<str:department_name>/', views.show_department_by_name),
    path('worker/<int:worker_id>/', views.show_worker_by_id),
]
