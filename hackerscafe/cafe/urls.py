from django.urls import path, re_path
from cafe import views

#Template Tagging
app_name = 'cafe'   #Use this Tag inside the html page to call the required URL

urlpatterns = [
#    re_path('^$', views.index, name="index"),
    re_path('^index/$', views.index, name="index"),
    re_path('^signup/$', views.signup, name="signup"),
    re_path('^members-list/$', views.memberslist, name="members-list"),
]


