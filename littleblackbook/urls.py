"""littleblackbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from littleblackbookapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^new', views.new, name="new"),
    url(r'^adduser', views.adduser, name="adduser"),
    # url(r'^newprofessional', views.newprofessional, name='newprofessional'),
    # url(r'^newcompany', views.newcompany, name='newcompany'),
    url(r'^review', views.review, name="review"),
    url(r'^edit/(?P<id>\d+)/', views.edit, name='edit'),
    url(r'^professional/(?P<id>\d+)/', views.professional, name='professional'),
    url(r'^displayall', views.displayall, name='displayall'),
    url(r'^socialfeed', views.socialfeed, name='socialfeed'),
]
