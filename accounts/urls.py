from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]