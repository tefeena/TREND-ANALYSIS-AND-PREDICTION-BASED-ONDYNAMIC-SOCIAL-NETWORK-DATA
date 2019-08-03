"""Twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from adminapp.views import *
from publicapp.views import *
from userapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #admin
    url(r'^index/$',index,name="index"),
    url(r'^view_users/$',view_users,name="view_users"),
    url(r'^approve/(?P<id>[0-9]+)',approve,name='approve'),
    url(r'^delete/(?P<id>[0-9]+)',delete,name='delete'),
    url(r'^view_ausers/$',view_ausers,name="view_ausers"),
    url(r'^view_search/$',view_search,name="view_search"),
    url(r'^view_contact/$',view_contact,name="view_contact"),
    url(r'^reply/(?P<id>[0-9]+)',reply,name="reply"),

    #public
    url(r'^$',home,name="home"),
    url(r'^about/$',about,name="about"),
    url(r'^terms/$',terms,name="terms"),
    url(r'^reg/$',reg,name="reg"),
    url(r'^rsuccess/$',rsuccess,name="rsuccess"),
    url(r'^log/$',log,name="log"),
    url(r'^error/$',error,name="error"),
    url(r'^logout/$',logout,name='logout'),
    url(r'^contact/$',contact,name="contact"),
    url(r'^csuccess/$',csuccess,name="csuccess"),


    #user
    url(r'^profile/$',profile,name="profile"),
    url(r'^edit/(?P<id>[0-9]+)',edit,name='edit'),
    url(r'^search/$',search,name="search"),
    url(r'^result/$',result,name="result"),
    url(r'^tweets/$',tweets,name="tweets"),
    url(r'^graph/$',graph,name="graph"),
    url(r'^user_contact/$',user_contact,name="user_contact"),
    url(r'^forgetpass/$',forgetpass,name="forgetpass"),

]
