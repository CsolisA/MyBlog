from django.urls import path
from blog import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('create-post', views.createPost, name='createPost'),
    path('insert-post', views.insertPost, name='insertPost'),
    path('search-post', views.searchPost, name='searchPost'),
    path('all-pages', views.allPages, name='allPages'),
    path('post/<int:id>', views.viewPage, name='viewPage'),
    path('my-posts', views.myPosts, name='myPosts'),
    path('modify-posts/<int:id>', views.modifyPost, name='modifyPosts'),
    path('delete-posts/<int:id>', views.deletePost, name='deletePost'),

    path('about-us', views.aboutUs, name='aboutUs'),

    path('login', views.login_request, name="login"),
    path('register', views.register, name="register"),
    path('profile', views.showProfile, name="showProfile"),
    path('edit-profile', views.editProfile, name="editProfile"),
    path('logout', views.logout_view, name='logout')

]
