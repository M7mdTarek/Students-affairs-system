from unicodedata import name
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import *
from .forms import loginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def home(request):
    return render(request, 'pages/pages/home.html')

def login2(request):
    return render(request, 'pages/pages/Log in.html')

def loginPage(request):
    if request.method == 'POST':
        usernam = request.POST.get('username')
        passwor = request.POST.get('password')
        user = authenticate(username= usernam, password= passwor)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, "Information invalid")
            return redirect("login")        
    return render(request, 'pages/pages/Log in.html')

def Add_student(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        id = request.POST.get('id')
        date = request.POST.get('date')
        gpa = request.POST.get('gpa')
        gender = request.POST.get('gender')
        level = request.POST.get('level')
        status = request.POST.get('status')
        dep = request.POST.get('dep')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
    
        info = student(name= username, Id= id, date= date, gpa=gpa, gender=gender, level=level, status=status, dep=dep, email=email, mobile = mobile)
        info.save()
        return HttpResponseRedirect(reverse('home'))

    return render(request, 'pages/pages/Add.html')

def Active(request):
    return render(request, 'pages/pages/Active-inactive.html',{'name':student.objects.all()})

def Add(request):
    return render(request, 'pages/pages/Add.html')

def Department(request):
    return render(request, 'pages/pages/Department.html')


def help(request):
    return render(request, 'pages/pages/help.html')


def edit(request,ID):
    stu = student.objects.get(Id=ID)
    return render(request, 'pages/pages/edit.html',{'stu':stu})

def Update(request,ID):
    if request.method == "POST":
        stu = student.objects.get(Id=ID)
        stu.name=request.POST.get('edit')
        stu.Id=request.POST.get('edit1')
        stu.date=request.POST.get('date')
        stu.gpa=request.POST.get('GPA')
        stu.gender=request.POST.get('gender')
        stu.dep=request.POST.get('dp')
        stu.level=request.POST.get('level')
        stu.email=request.POST.get('e-mail')
        stu.mobile=request.POST.get('mobile')
        stu.save()

        return HttpResponseRedirect(reverse('Active'))

def LogoutPage(request):
    logout(request)
    return redirect('login')


def Dep(request,ID):
    stu = student.objects.get(Id=ID)
    return render(request, 'pages/pages/edit.html',{'stu':stu})

def DepUpdate(request,ID):
    if request.method == "POST":
        stu = student.objects.get(Id=ID)
        stu.name=stu.name
        stu.Id= stu.Id
        stu.date=stu.date
        stu.gpa=stu.gpa
        stu.gender=stu.gender
        stu.dep=request.POST.get('dp')
        stu.level=request.POST.get('level')
        stu.email=stu.email
        stu.mobile=stu.mobile
        stu.save()

        return HttpResponseRedirect(reverse('Active'))

def searchPage(request):
    return render(request, 'pages/pages/search.html')

def search(request):

    if request.method == "GET":
        search = request.GET.get('search')
        data = []
        if search is not None:
            search = request.GET.get('search')
            stu = student.objects.all().filter(name__contains = search)
            for x in stu:
                I = {
                    'name':x.name,
                    'ID':x.Id,
                }
                data.append(I)
            print(data)
        else:
            data = []
        
        return JsonResponse({'stu':data})


def deleteStudent(request,Id):
    stu=student.objects.get(Id=Id)
    stu.delete()
    return JsonResponse({"messages":"success"})