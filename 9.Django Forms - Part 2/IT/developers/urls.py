from django.urls import path
from IT.developers import views


urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:developer_id>/', views.update_name, name='update'),
    path('success/', views.success, name='success'),
    path('devs/', views.developers, name='devs')
]
