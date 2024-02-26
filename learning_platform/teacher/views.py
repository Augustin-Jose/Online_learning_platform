from django.db.models import Q
from django.shortcuts import render

from login.models import Login
from teacher.models import Teacher


def teacher(request):
    obk=""
    a=request.POST.get('email')
    obv=Teacher.objects.filter(Q(email=a)& Q(email=a))
    if len(obv)>0:
        obk="email exist"

    else:
        if request.method == 'POST':
            obj = Teacher()
            obj.name = request.POST.get('name')
            obj.password = request.POST.get('password')
            obj.confirm_password = request.POST.get('confirm_password')
            obj.email = request.POST.get('email')
            obj.resume = request.POST.get('resume')
            obj.certificate = request.POST.get('certificate')
            obj.subject = request.POST.get('subject')
            obj.save()
    context = {
        'x': obk
    }

    return render(request,'teacher/teacher.html',context)





def adm_man_teacher(request):
    obj=Teacher.objects.all()
    context={
        'a':obj
    }


    return render(request,'teacher/adminmanage_teacher.html',context)

def approve(request, idd):
    obj = Teacher.objects.get(teacher_id=idd)
    obj.status = 'approved'
    obj.save()
    ob = Login()
    ob.username = obj.email
    ob.password = obj.password
    ob.type = 'teacher'
    ob.u_id = obj.teacher_id
    ob.save()
    return adm_man_teacher(request)

def reject(request, idd):
    obj = Teacher.objects.get(teacher_id=idd)
    obj.status = 'rejected'
    obj.save()
    obb=Login.objects.get(u_id=idd, type='teacher')
    obb.delete()
    return adm_man_teacher(request)