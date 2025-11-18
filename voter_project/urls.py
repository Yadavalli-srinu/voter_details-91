"""
URL configuration for voter_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app1.views import (register_form,login1_form,home,voter_user_table,voter_user_empty_form,voter_user_update_form,voter_user_delete,
                        voter_profile_table,voter_profile_empty_form,voter_profile_update_form,voter_profile_delete)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",register_form,name="reg101"),
    path("log101/",login1_form,name="log101"),
    path("home101/",home,name='home101'),
    path("user_table",voter_user_table,name='usertable'),
    path("user_empty/",voter_user_empty_form,name='user_empty'),
    path("user_update/<int:id>/",voter_user_update_form,name='user_update'),
    path("user_delate/<int:id>/",voter_user_delete,name='user_delate'),


    path("profile_table/",voter_profile_table,name='profiletable'),
    path("profile_empty/",voter_profile_empty_form,name='profile_empty'),
    path("profile_update/<int:id>/",voter_profile_update_form,name='profile_update'),
    path("profile_delate/<int:id>/",voter_profile_delete,name='profile_delate')
]
