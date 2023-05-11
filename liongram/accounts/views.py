from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import UserCreateForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def singup_view(request):
    if request.method == 'GET':
        form = SignUpForm
        context = { 'form' : form}
        return render(request,'accounts/singup.html',context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('index')
        else:
            return redirect('accounts:signup')

def login_view(request):
    #GET, POST
    if request.method == 'GET':
        return render(request, 'accounts/login.html',{'form':AuthenticationForm()})
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('index')
