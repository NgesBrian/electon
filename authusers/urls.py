from django.urls import path

from . import views

app_name = "authusers"
urlpatterns = [
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('elections', views.elections, name='elections'),
    path('election/<id>', views.election, name='election'),
    path('vote/<id>', views.vote, name='vote'),
    path('results', views.results, name='results'),
     path('result<id>', views.result, name='result'),
]