from django.contrib.auth import login, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import RegisterForm, User, AuthenticationForm

def register_view(request:HttpRequest):
    if request.method =='POST':
        form=RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hisob muvaffaqiyatli ochildi')
            return redirect('login')
    else:
        form=RegisterForm()
    context={
        'form':form
    }
    return render(request, 'user/register.html', context)

def login_view(request:HttpRequest):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Tizimga muvaffaqiyatli kirdingiz')
            return redirect('home')
    else:
        form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request, 'user/register.html', context)

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.warning(request, 'Tizimdan  muvaffaqiyatli chiqdingiz')
    return redirect('login')

