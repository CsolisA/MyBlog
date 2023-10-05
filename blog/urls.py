from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create-post', views.createPost, name='createPost'),
    path('insert-post', views.insertPost, name='insertPost'),
    path('search-post', views.searchPost, name='searchPost'),
]
