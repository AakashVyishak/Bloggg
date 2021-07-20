from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.


def register(request):
    if request.method=="POST":
        first_name =request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        username=request.POST['username']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name= last_name,email=email,password=password)
                user.save();
                print("user created")
        else:
            print("user not created")

        return redirect('/')
    else:
        return render(request,"register.html")
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
    else:
        messages.info(request,'invalid details')
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
