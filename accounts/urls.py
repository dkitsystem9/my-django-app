from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),

]
