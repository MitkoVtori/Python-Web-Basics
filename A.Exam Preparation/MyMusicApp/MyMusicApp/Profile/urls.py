from django.urls import path
from MyMusicApp.MyMusicApp.Profile import views

urlpatterns = [
    path('details/', views.profile_details, name='profile'),
    path('delete/', views.delete_profile, name='delete profile')
]
