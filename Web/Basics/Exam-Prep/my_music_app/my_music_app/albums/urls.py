from django.urls import path, include
from my_music_app.albums import views


urlpatterns = [
    path('add/', views.add_album, name='album_add'),
    path('<int:pk>/', include([
        path('details/', views.show_album_details, name='album_details'),
        path('edit/', views.edit_album, name='album_edit'),
        path('delete/', views.delete_album, name='album_delete'),
]))
]
