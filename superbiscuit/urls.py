"""superbiscuit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from biscuit import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^business/$', views.business_home, name='business_home'),
    url(r'owner_list_add/', views.owner_list_add, name='owner_list_add'),
    url(r'client_metrics/', views.client_metrics, name='client_metrics'),
    url(r'client_list/', views.client_list, name='client_list'),
    url(r'client_indiv/', views.client_indiv, name='client_indiv'),
    url(r'walker_metrics/', views.walker_metrics, name='walker_metrics'),
    url(r'walker_list/', views.walker_list, name='walker_list'),
    url(r'walker_indiv/(?P<walker_id>[0-9]{2})/$', views.walker_indiv, name='walker_indiv'),
    url(r'appointment_calendar/', views.appointment_calendar,
        name='appointment_calendar'),
    url(r'appointment_list/', views.appointment_list,
        name='appointment_list'),

    #url(r'^new_busines/', views.new_business, name='new_business'),

)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
