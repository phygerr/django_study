#encoding:utf-8
# Create your views here.
from django.shortcuts import render,redirect,HttpResponseRedirect
from models import Person,Account
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# 第四个auth是用户权限有关的类。auth可以设置每个用户的权限。
from .forms import UserForm
import time

def insert(request):
    return render(request,'insert.html')
def do(request):
    username = request.POST['username']
    userage = request.POST['userage']
    context = {'username':username,'userage':userage}
    Person.objects.get_or_create(name=username,age=userage)
    all=Person.objects.all()
    return render(request,'do.html',{'context':context,'all':all})
def index(request):
    return render(request,'index.html')
def get1(request):
    return render(request,'get1.html')
def get2(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    phone = request.POST['phone']
    context = {'username':username,'password':password,'email':email,'phone':phone}
    Account.objects.get_or_create(username=username,password=password,email=email,phone=phone)
    all=Account.objects.all()
    return render(request,'get2.html',{'context':context,'all':all})
def search1(request):
    return render(request,'search_result.html')
def search(request):
    keyword=request.GET['keyword']
    person=Person.objects.filter(Q(name__contains=keyword)|Q(age__contains=keyword))
    # pp=[]
    # aa=[]
    # for i in person:
    #     pp.append(i.name)
    #     aa.append(i.age)
    # rr=zip(pp,aa)
    # return render(request,'search_result.html',{'rr':rr})
    return render(request,'search_result.html',{'pp':person})

