from django.urls import path

from django.conf.urls import url
from voting import views as reg_views

from . import views

app_name = "voting"
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    #path('signup', views.signup, name='signup'),
    #path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    url(r'^update_profile', views.update_profile, name='update_profile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        reg_views.activate, name='activate'),
]