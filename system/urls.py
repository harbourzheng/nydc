from django.conf.urls import patterns, url

from system import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.main, name='main'),
    url(r'/profile/^$',views.profile,name='profile'),
    (r'^/search_form/$', views.search_form,name='search_form'),
    (r'^/search/$', views.search,name='search'),
    #url(r'/searchPage/^$',views.searchPage,name='searchPage'),
    #url(r'/search/^$',views.search,name='search'),
    #url(r'/money/^$',views.money,name='money'),
)