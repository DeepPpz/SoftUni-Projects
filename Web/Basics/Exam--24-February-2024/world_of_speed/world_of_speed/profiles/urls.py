from django.urls import path
from world_of_speed.profiles import views


urlpatterns = [
    path('create/', views.create_profile, name='profile_create'),
    path('details/', views.show_profile_details , name='profile_details'),
    path('edit/', views.edit_profile , name='profile_edit'),
    path('delete/', views.delete_profile , name='profile_delete'),
]
