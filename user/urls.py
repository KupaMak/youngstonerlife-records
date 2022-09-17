from django.urls import path
from . import views

urlpatterns = [
    path('albums', views.albums, name='user-albums'),
    path('logouturls', views.login, name='user-logout'),
    
]
