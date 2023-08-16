from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForms
from .models import Records

# Create your views here.
def home(request):
    records = Records.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in...")
            return redirect('home')
        else:
            messages.success(request, "Login failed. Please retry again..")
    return render(request, 'home.html',{'records':records})



def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully..")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request,user)
            messages.success(request, "You have been registered successfully.. Welcome!")
            return redirect('home')
        
    else:
        form = SignUpForms()
        return render(request, 'register.html',{'form':form})

    return render(request, 'register.html',{'form':form})