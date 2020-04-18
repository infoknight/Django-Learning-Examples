from django.urls import path, re_path
from winforen import views

#Template Tagging
app_name = 'winforen'   #Use this Tag inside the html page to call the required URL

urlpatterns = [
#    re_path('^$', views.index, name="index"),
    re_path('^index/$', views.index, name="index"),
    re_path('^register/$', views.register, name="register"),
    re_path('^members-list/$', views.memberslist, name="members-list"),
#    re_path('^user_login/$', views.user_login, name="user_login"),
]


