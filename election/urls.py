"""election URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from django.contrib.auth import views as auth_views
from voting import views as reg_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("voting.urls")),
    path('', include("authusers.urls")),
    path('login/', auth_views.login, {'template_name': 'voting/login.html'}, name='login'),
    path('logout/', auth_views.logout,{'next_page': '/'}, name='logout'),
    url(r'^signup/$', reg_views.signup, name='signup'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^account_activation_sent/$', reg_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        reg_views.activate, name='activate'),
    # password change url definitions
    url(r'^accounts/password/change/$', auth_views.password_change, {
        'template_name': 'registration/password_change_form.html'},
        name='password_change'),
    url(r'^accounts/password/change/done/$', auth_views.password_change_done,
        {'template_name': 'registration/password_change_done.html'},
        name='password_change_done'),
]