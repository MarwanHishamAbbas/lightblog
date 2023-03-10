from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User


def userAuth(request):
    form = CreateUserForm()
    if request.method == 'POST':
        if 'sign-up' in request.POST:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request,'Password must be strong')
                return redirect('auth')

                
        if 'sign-in' in request.POST:
            email = request.POST.get('email').lower()
            password = request.POST.get('password')
            try:
                user = User.objects.all()
            except:
                print("Can't find the user in the database")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request,'Email or password not correct')
                return redirect('auth')
 

    context = {'form': form}
    return render(request, 'auth.html', context)

def home(request):
    context = {}
    return render(request, 'base.html', context)