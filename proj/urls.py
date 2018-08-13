"""proj URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from people import views as vv
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^insert/$', vv.insert),
    url(r'^do/$', vv.do),
    url(r'^get1/$', vv.get1),
    url(r'^get2/$', vv.get2),
    url(r'^search1/$',vv.search1),
    url(r'^search/$',vv.search),
    url('^$', vv.index),

]
