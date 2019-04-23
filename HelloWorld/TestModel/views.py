from django.shortcuts import render
from . import models

def index(request):
    return render(request,'TestModel/index.html',locals())


def detail(request,blog_id):

    return render(request,'TestModel/detail.html',locals())

def lists(request):
    movie_list=models.Test.objects.all()
    return render(request,'TestModel/show.html',{"movie_list":movie_list})

def phone_msg(request):
    phone_list=models.phone.objects.all()
    return render(request,'TestModel/selemiun_show.html',{"phone_list":phone_list})