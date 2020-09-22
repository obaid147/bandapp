from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('home', views.index, name="home"),
    path('members', views.members, name="members"),
    path('members/uploads#uploads', views.members, name="members/uploads"),
    path('videos', views.videos, name="videos"),
    path('about', views.about, name="about"),
    path('downloads', views.download, name='downloads'),
    path('<int:pk>', views.delete, name='delete'),
]