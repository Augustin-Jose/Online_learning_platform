from django.shortcuts import render
from teacher.models import Teacher


def teacher(request):
    if request.method == 'POST':
        obj = Teacher()
        obj.name = request.POST.get('name')
        obj.password = request.POST.get('password')
        obj.qualification = request.POST.get('qualification')
        obj.subject = request.POST.get('subject')

        obj.save()
    return render(request,'teacher/teacher.html')



def add_teacher(request):
    return render(request,'teacher/add teacher.html')



def adm_man_teacher(request):
    return render(request,'teacher/adminmanage_teacher.html')