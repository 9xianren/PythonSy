from django.shortcuts import render
from TestModel import models
  
def login(request):
    adminlist=models.admin.opject.all()
    return render(request,'TestModel/login.html',{"adminlist":adminlist})