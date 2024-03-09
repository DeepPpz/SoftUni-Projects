from django.urls import path, include
from my_music_app.common import views


urlpatterns = [
    path('', views.show_homepage, name='homepage'),
]
