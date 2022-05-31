from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from .decorator import superuser_required

def loginuser(request):
    if request.method == "POST":
        mobile = request.POST['mobile']
        password = request.POST['password']
    # try:
    #     user = User.objects.get(mobile=mobile)
    # except:
        user = authenticate(request, mobile=mobile, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse(" Username & password is incorrect")

    return render(request, 'login.html')  

def logoutUser(request):
    logout(request)
    return redirect('loginuser')

def alluser(request):
    user = User.objects.all()
    context = {"user":user}
    return render(request, 'alluser.html', context)
    
def dashboard(request):
    return render(request, "dashboard.html")


def update_profile(request):
    if request.method == "POST":
       if request.user.is_superuser == True:
            profile = UserForm(request.POST, instance=request.user)
       else:
            profile = UserForm(request.POST, instance=request.user)    
    if profile.is_valid():
        profile.save()
    else:
        HttpResponse('You are not a superuser, So not update the profile')
    context = {'profile':profile}
    return render(request, 'signup.html', context)

def registerUser(request):
    print("User", request.user)
    if request.method == "POST":
        print("RES", request.POST)
        try:
            mob = User.objects.get(mobile=request.POST['mobile'])
            context = {
                'mob':mob,
            }
            return render(request, 'signup.html', context)
        except User.DoesNotExist:    
            mob = User.objects.create(mobile=request.POST['mobile'],username=request.POST['username'] ,password=request.POST['password'])
            login(request, mob)
            mob.save()
            return redirect('home')
    else:
        HttpResponse('An error has come during registration. please check Mobile & password') 
    return render(request, 'signup.html')    
  
def createUser(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.save()

            return redirect('login')
    context = {'form':form}    
    return render(request, "", context)

def updateUser(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        if request.user.is_superuser == True:
            profile = User.objects.get(request.POST, instance=user)
            profile.save()

            return redirect('alluser')

    context = {'user':user}
    return render(request, "alluser.html", context)

def singleuser(request, id):
    # user = User.objects.get(id=request.GET.get(id))
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user = User(instance=user)
        user.save()
        return redirect('alluser')
    context = {'user': user}
    return render(request, 'singleuser.html', context)

