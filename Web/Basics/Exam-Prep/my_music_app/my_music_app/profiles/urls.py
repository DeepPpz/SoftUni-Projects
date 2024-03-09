from django.urls import path
from my_music_app.profiles import views


urlpatterns = [
    path('details/', views.show_profile_details, name='profile_details'),
    path('delete/', views.delete_profile, name='profile_delete'),
]
