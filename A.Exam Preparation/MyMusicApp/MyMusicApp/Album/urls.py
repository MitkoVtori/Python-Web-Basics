from django.urls import path
from MyMusicApp.MyMusicApp.Album import views

urlpatterns = [
    path('add/', views.add_album, name='add album'),
    path('details/<int:id>/', views.album_details, name='album details'),
    path('edit/<int:id>/', views.edit_album, name='edit album'),
    path('delete/<int:id>/', views.delete_album, name='delete album')
]
