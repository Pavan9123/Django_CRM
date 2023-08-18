from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForms,RecordsForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
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

def customer_record(request, pk):
    if request.user.is_authenticated:
        #Look up Records
        record = Record.objects.get(id = pk)
        return render(request, 'record.html',{'record':record})
    else:
        messages.success(request, "You must login first to view the records")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id = pk)
        print(delete_it)
        delete_it.delete()
        messages.success(request, "Record has been deleted successfully.")
        return redirect('home')
    else:
        messages.success(request, "You must login first to view the records")
        return redirect('home')
    
def add_record(request):
    form = RecordsForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Your details has been added to records")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
