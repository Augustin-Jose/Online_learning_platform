from django.db.models import Q
from django.shortcuts import render

from login.models import Login
from teacher.models import Teacher
import requests

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
            obj.phn=request.POST.get('phn')
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


    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = "message=Edufy Your Registration for teacher have been approved  &language=english&route=q&numbers="+obj.phn
    headers = {
        'authorization': "HnyPTzX9GKetEMLq8Z7AhaCQOW56pJdYwNIbj024kfRVcs3oDi1imxIYGfhsjSWVDu3HMbXO2CLvq0eA",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
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
    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = "message= Edufy Your Registration for teacher have been rejected &language=english&route=q&numbers=" + obj.phn
    headers = {
        'authorization': "HnyPTzX9GKetEMLq8Z7AhaCQOW56pJdYwNIbj024kfRVcs3oDi1imxIYGfhsjSWVDu3HMbXO2CLvq0eA",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    obb=Login.objects.get(u_id=idd, type='teacher')
    obb.delete()
    return adm_man_teacher(request)