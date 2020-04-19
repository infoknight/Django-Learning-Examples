"""hackerscafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import url, include
from cafe import views

urlpatterns = [
    re_path('^$', views.index, name="index"),
    path('admin/', admin.site.urls),
    re_path('^cafe/', include('cafe.urls')),
    re_path('^logout/$', views.user_logout, name="logout"),
    re_path('^special/', views.special, name="special"),        #Redirect the loggedin user to the special page; @login_required
]

'''
urlpatterns = [
    re_path('^$', views.index, name="index"),
    path('admin/', admin.site.urls),
    re_path('^signup/', views.signup, name="signup"),
    re_path('^members-list/', views.memberslist, name="memberslist"),
]
'''


