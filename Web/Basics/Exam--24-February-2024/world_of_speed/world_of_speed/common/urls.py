from django.urls import path
from world_of_speed.common import views


urlpatterns = [
    path('', views.show_index_page, name='index'),
]
