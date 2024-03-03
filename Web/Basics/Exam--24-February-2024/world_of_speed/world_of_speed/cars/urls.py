from django.urls import path, include
from world_of_speed.cars import views


urlpatterns = [
    path('catalogue/', views.show_cars_catalogue, name='cars_catalogue'),
    path('create/', views.create_car, name='car_create'),
    
    path('<int:pk>/', include([
        path('details/', views.show_car_details, name='car_details'),
        path('edit/', views.edit_car_details, name='car_edit'),
        path('delete/', views.delete_car, name='car_delete'),
        ])),
]
