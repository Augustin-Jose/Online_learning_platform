from django.shortcuts import render
from login.models import Login

# Create your views here.

def login(request):
    if request.method == 'POST':
        obj = Login()
        obj.username = request.POST.get('username')
        obj.password = request.POST.get('password')
        obj.user_id=request.POST.get('user_id')
        obj.save()
    return render(request, 'login/login.html')
