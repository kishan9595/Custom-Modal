from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, "dashboard.html")

def user_profile(request):
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
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        print("RES", request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.mobile = user.mobile
            # user.email = user.email
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, email=email, password=password)
            # user.password = make_password(user.password)
            user.save()

            login(request, user)
            return redirect('home')

        else:
            HttpResponse('An error has come during registration. please check Mobile & password')

    context = {'form':form}
    return render(request, 'signup.html', context)

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


def createUser(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.save()

            return redirect('login')
    context = {'form':form}    
    return render(request, "", context)

def updateUser(request, pk):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()

            return redirect('')

    context = {'form':form, 'user':user}
    return render(request, "", context)

def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('')

    context = {'object': user}
    return render(request, '', context)

