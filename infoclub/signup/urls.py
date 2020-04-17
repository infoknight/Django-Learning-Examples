from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, re_path
from signup import views

#Template Tagging
app_name = 'club'       #Use this tag inside html to call the required URL

urlpatterns = [
    re_path('^$', views.index, name="index"),
    re_path('^datasheet/$', views.datasheet, name="datasheet"),
    re_path('^register/$', views.register, name="register"),
]
