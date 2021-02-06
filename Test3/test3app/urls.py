"""test3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.demo, name='demo'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('Logout', views.Logout, name='Logout'),
    path('reg', views.reg, name='reg'),
    path('uploadcsv', views.upload, name='upload'),
    path('registration', views.handelreg, name="registration"),
  # path('display', views.display, name="display"),
    path('show', views.show, name="show"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('destroy/<int:id>', views.destroy, name="destroy"),
    path('search', views.searchposts, name="search"),
    path('AdminTable', views.AdminTable, name="AdminTable"),
    path('adminreg', views.adminreg, name="adminreg"),
    path('delete', views.delete, name="delete"),
    path('visualization', views.visualization, name="visualization"),
]
