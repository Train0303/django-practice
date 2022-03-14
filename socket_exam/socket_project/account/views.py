from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        request.session['email'] = email
        print(email,password)
        user = authenticate(username=email, password=password)
        if user:
            print("login success")
            auth_login(request,user=user)
            return redirect('chat:index')
    return render(request, 'account/login.html')

@csrf_protect
def logout(request):
    auth_logout(request)
    return redirect('chat:index')