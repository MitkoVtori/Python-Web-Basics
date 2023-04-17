from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index),
    path('Programming-basics/5432/course', views.basics),
]

urlpatterns += staticfiles_urlpatterns()
