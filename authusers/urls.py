from django.urls import path

from . import views

app_name = "authusers"
urlpatterns = [
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('elections', views.elections, name='elections'),
    path('results', views.results, name='results'),
]