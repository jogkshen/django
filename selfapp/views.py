from django.shortcuts import render,HttpResponse, redirect
from selfapp.models import person
from selfapp.models import registered_user
import os


# Create your views here.
def home(request):
    return HttpResponse ("hi this is home page for my self")


def naya(request):
    return render(request, 'dashboard.html')

def ghar(request):
    return render(request, 'ghar.html')
 
def addobject(request):
    obj = person.objects.get (
        name="name", age="" , is_student=True, email="jpt@gmail.com", message=""
    )
    obj.save()
    return HttpResponse ('add')

def registration(request):
    return render(request, 'registration.html')

def register(request):
    if request.method =='POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        photo = request.FILES.get('photo')


        obj= registered_user.objects.create(
            fullname = fullname,
            email = email,
            password = password,
            confirm_password = confirm_password,
            photo = photo
            )
        
        obj.save()
        return HttpResponse('value added !')
    ob=registered_user.objects.all()
    return render(request,'registration.html',{'obj':ob})

def dashboard(request):
    obj = registered_user.objects.all()
    return render(request, 'dashboard.html', {'obj':obj})

def register_update(request,key):
    obj = registered_user.objects.get(id=key)

    if request.method=="POST":
        obj.fullname = request.POST.get('fullname')
        obj.email = request.POST.get('email')
        obj.password = request.POST.get('password')
        obj.confirm_password = request.POST.get('confirm_password')
        if 'photo' in request.FILES:
            obj.photo = request.FILES.get('photo')

        obj.save()
        return HttpResponse('value updated')
    return render(request, 'registerupdate.html',{'obj':obj})
 

def deleteuser(request,key):
    obj = registered_user.objects.get(id=key)
    obj.delete()
    return redirect('registration')
 

def loginpage(request, u_id):
    obj = registered_user.objects.get(id=u_id)

    if request.method=="POST" and obj.fullname = registered_user.POST.get('fullname'):
        
        obj.password = registered_user.POST.get('password')



    return render(request, 'login.html')
    

        



