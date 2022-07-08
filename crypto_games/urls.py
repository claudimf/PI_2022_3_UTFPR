from django.urls import path

from . import views


app_name = 'crypto_games'

urlpatterns = [
    path('profile', views.profile, name='profile'),
]
