from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
from django.contrib import messages

def home(request):
    return render(request,'app1/index.html')


def user_registration(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'user created successfully')
            return redirect('login')
        else:
            messages.error(request,'Invalid details')
           
    else:
        form=UserForm()
    return render(request,'app1/signup.html',{'form':form})
