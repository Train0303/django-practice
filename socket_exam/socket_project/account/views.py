from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_protect

from .models import User

@csrf_protect
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        request.session['email'] = email
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

@csrf_protect
def signup(request):
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                User.objects.get(email=request.POST.get('email'))
                return render(request, 'account/signup.html') 
            except:
                try:
                    User.objects.get(email=request.POST.get('username'))
                    return render(request, 'account/signup.html') 
                except:
                    user = User.objects.create_user(email=request.POST.get('email'),
                                                username=request.POST.get('username'),
                                                password=request.POST.get('password1'))
                    auth_login(request,user)
                    print("생성완료")
                    return redirect("chat:index")  
                              
    print("생성실패2")
    return render(request, 'account/signup.html')