from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nydc.views.home', name='home'),
    # url(r'^nydc/', include('nydc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/', include('system.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    )

