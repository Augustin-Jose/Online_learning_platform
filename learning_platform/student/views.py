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

def student_edit(request,idd):
    ob = Student.objects.get(student_id=idd)
    context = {
        'e': ob,
    }
    if request.method == 'POST':
        obj = Student.objects.get(student_id=idd)
        obj.name = request.POST.get('name')
        obj.password = request.POST.get('password')
        obj.age = request.POST.get('age')
        obj.gender = request.POST.get('gender')
        obj.address = request.POST.get('address')
        obj.status = 'pending'
        obj.save()
        return admin_man_user(request)
    return render(request, 'student/studentedit.html',context)


def admin_man_user(request):
    obj = Student.objects.all()
    context = {
        'a': obj
    }
    return render(request, 'student/adm_man_user.html',context)

def edit(request,idd):
    obj = Student.objects.get(student_id=idd)
    obj.status = 'edited'
    obj.save()
    return admin_man_user(request)



def delete(request,idd):
    obj = Student.objects.get(student_id=idd)
    obj.status = 'deleted'
    obj.delete()
    return admin_man_user(request)