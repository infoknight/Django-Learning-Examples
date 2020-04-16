from django.contrib import admin
from django.urls import path, re_path
from signup import views

urlpatterns = [
    re_path('^$', views.index, name="index"),
]
