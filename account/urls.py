from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',

    url(r'^login/$', views.login, name='login'),
    url（r'^auth/$', views.auth, name='auth_view'）,
    url（r'^auth/$', views.auth, name='logout'）,
    url（r'^auth/$', views.auth, name='logged'）,
    url（r'^auth/$', views.auth, name='invalid'）,
)