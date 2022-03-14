from django.shortcuts import redirect, render
import sys,os
from django.contrib.auth import authenticate 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "chat/index.html", {})
    return redirect("account:login")

def room(request, room_name):
    if request.user.is_authenticated:
        return render(request, "chat/room.html",{
            'room_name' : room_name
        })
    return redirect("account:login")