from django.urls import path

from DjangoForms.TestForms import views


urlpatterns = [
    path('', views.index, name='index'),
    path('successful/', views.successful_form_fill, name='success'),
]
