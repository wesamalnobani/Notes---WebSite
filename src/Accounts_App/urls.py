from django.urls import path
from .views import accounts,register_users,register_backend,login_user,login_user_backend,user_profile,logout_user,change_password
from django.contrib.auth import login, logout
urlpatterns = [
    path('',accounts),
    path('register_users/',register_users,name='register_users'),
    path('register_backend/',register_backend,name='register_backend'),
    path('login_user/',login_user,name='login_user'),
    path('login_user_backend/',login_user_backend,name='login_user_backend'),
    path('user_profile/<str:user>/',user_profile,name='user_profile'),
    path('logout_user/',logout_user,name='logout_user'),
    path('user_profile/<str:user>/change_password/',change_password,name='change_password'),
]
