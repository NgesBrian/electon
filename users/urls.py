from django.urls import path
from django.conf.urls import url
from . import views

app_name = "users"
urlpatterns = [
    path('home', views.home, name='home'),
    path('dashboard', views.home, name='dashboard'),
 ]
