from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_profile, name="create profile"),
    path('details/', views.profile_details, name='profile details'),
    path('edit/', views.profile_edit, name='edit profile'),
    path('delete/', views.delete_profile, name='delete profile')
]
