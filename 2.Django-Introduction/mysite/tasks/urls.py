from django.urls import path
from mysite.tasks.views import tasks, diets


urlpatterns = (
    path('', tasks),
    path('diets/', diets),
)
