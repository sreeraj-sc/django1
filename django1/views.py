from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *

def index(request):
    return render(request, 'index.html')
    
def adduser(request):
    if request.method == 'POST' :
        a = request.POST.get('name')
        b = request.POST.get('age')
        c = request.POST.get('email')
        d = request.POST.get('password')
        e = regtable(name=a, age=b, email=c, password=d)
        e.save()
    return render(request, 'index.html')

def updateuser(request, id):
    a = regtable.objects.get(id = id)
    return render(request, 'updateuser.html',{'result': a})

def update(request, id):
    if request.method == 'POST' :
        a = request.POST.get('name')
        b = request.POST.get('age')
        c = request.POST.get('email')
        d = request.POST.get('password')
        e = regtable(name=a, age=b, email=c, password=d, id = id)
        e.save()
    return redirect(viewuser)

def viewuser(request):
    a = regtable.objects.all()
    return render(request,'view.html',{'result': a})

def updateuser(request, id):
    a = regtable.objects.get(id = id)
    return render(request, 'updateuser.html',{'result': a})

def deleteuser(request, id):
    a = regtable.objects.get(id = id)
    a.delete()
    return redirect(viewuser)

def login(request):
    return render(request, 'login.html')

def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password == 'admin' :
        request.session['admin'] = 'admin'
        return redirect(viewuser)
    elif regtable.objects.filter(email = email, password = password).exists():
        a = regtable.objects.get(email = email, password = password)
        request.session['uid'] = a.id
        return redirect(viewuser)
    else:
        return render(request, 'login.html')
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys :
        del request.session[key]
    return redirect(index)