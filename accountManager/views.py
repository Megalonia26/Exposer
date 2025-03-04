from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from django.contrib import messages

def userLogin(request):

    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username or Password is Incorrect")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, "accountManager/login.html")

def userRegister(request):
    if request.method == "POST":

        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")

        if len(password) <= 8:
            messages.error(request, "Password  To Short")
        elif password != password1:
            messages.error(request, "Password didn't match")
        else:
            try:
                user = User.objects.create_user(email=email, username=username, password=password)
                user.save()
                return redirect("user-login")
            except:
                messages.error(request, "An error seems occured during User creation proccess. Pleas Try again later")
    return render(request, "accountManager/register.html")

def userLogout(request):
    logout(request)
    return redirect("user-login")