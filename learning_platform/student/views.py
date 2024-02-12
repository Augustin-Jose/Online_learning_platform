from django.shortcuts import render

from login.models import Login
from student.models import Student


def student(request):
    if request.method == 'POST':
        obj = Student()
        obj.name = request.POST.get('name')
        obj.password = request.POST.get('password')
        obj.age = request.POST.get('age')
        obj.gender = request.POST.get('gender')
        obj.email = request.POST.get('email')
        obj.status='pending'
        obj.save()
        ob=Login()
        ob.username=obj.name
        ob.password=obj.password
        ob.type = 'student'
        ob.u_id=obj.student_id
        ob.save()

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
        obj.email = request.POST.get('email')
        obj.status = 'pending'
        obj.save()
        ob=Login.objects.get(u_id=request.session["u_id"],type='student')
        ob.password=obj.password
        ob.username=obj.name
        ob.save()
        return admin_man_user(request)
    return render(request, 'student/studentedit.html',context)


def admin_man_user(request):
    ss= request.session["u_id"]
    obj = Student.objects.filter(student_id=ss)
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

def ad_v_stud(request):
    obj = Student.objects.all()
    context = {
        'a': obj
    }
    return render(request, 'student/ad_v_stud.html',context)