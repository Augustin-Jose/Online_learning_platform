from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login

# Create your views here.

def login(request):
    if request.method == 'POST':

        uname = request.POST.get("username")
        passw = request.POST.get("password")
        obj = Login.objects.filter(username=uname, password=passw)
        tp = ""

        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "admin":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp == "student":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/student_home/')
            elif tp == "teacher":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/teacher_home/')
        else:
            objlist = "username or password incorrect"
            context = {
                'x': objlist,
            }
            return render(request, 'login/login.html', context)

    return render(request, 'login/login.html')

from django.http import JsonResponse
def check(requst):
    un=requst.GET.get('username')
    objs=Login.objects.filter(username=un)
    res='not'
    # print('hello')
    if len(objs)>0:
        res='exist'
    msg = {

        'msg': res
    }
    return JsonResponse(msg)