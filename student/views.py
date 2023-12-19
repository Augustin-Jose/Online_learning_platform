from django.shortcuts import render
from student.models import  Student


def student(request):
    if request.method == 'POST':
        obj = Student()
        obj.name = request.POST.get('name')
        obj.password = request.POST.get('password')
        obj.age = request.POST.get('age')
        obj.gender= request.POST.get('gender')
        obj.address = request.POST.get('address')
        obj.status='pending'
        obj.save()
    return render(request,'student/student.html')



def admin_man_user(request):
    return render(request, 'student/adm_man_user.html')