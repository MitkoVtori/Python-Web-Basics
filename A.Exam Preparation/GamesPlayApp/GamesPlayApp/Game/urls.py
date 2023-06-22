from django.urls import path
from GamesPlayApp.Game import views


urlpatterns = [
    path('create/', views.create_game, name='create game'),
    path('details/<int:id>/', views.game_details, name='game details'),
    path('edit/<int:id>/', views.edit_game, name='edit game'),
    path('delete/<int:id>/', views.delete_game, name='delete game')
]
