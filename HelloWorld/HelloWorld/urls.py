"""HelloWorld URL Configuration

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
from django.conf.urls import *
from django.contrib import admin
from django.views.generic.base import View
from django.shortcuts import render
from django.shortcuts import redirect
from TestModel import models
from . import view
from django.http import HttpResponse



class  IndexView(View):
    def get(self,request):
        return render(request,'TestModel/index.html')

class LoginView(View):
    def get(self,request):
        return render(request,'TestModel/login.html')

    def post(self,request):
        adminlist=models.admin.objects.filter()
        print(request.POST)
        username=request.POST.get("username",None)
        pwd=request.POST.get("pwd",None)
        print(username,pwd)

        for admin in adminlist:
            if username==admin.adminkey and pwd==admin.adminpwd:
                request.session['username']="管理员"
                request.session.set_expiry(600)
                return redirect("/TestModel/")
            else:

                error_msg="用户名或者密码错误"
                return render(request,"login.html",{"error":error_msg})

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^TestModel/',include('TestModel.urls'),name='TestModel'),
    url(r'^$',LoginView.as_view(),name='login')
]
