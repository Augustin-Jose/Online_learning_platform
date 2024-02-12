from django.shortcuts import render
from doubts.models import Doubts
import datetime
def doubts(request):
    ss=request.session["u_id"]
    if request.method == 'POST':
        obj = Doubts()
        obj.doubt = request.POST.get('doubt')
        obj.student_id=ss
        obj.reply = 'pending'
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.save()
    return render(request, 'doubts/doubts.html')

def reply(request,idd):

    if request.method == 'POST':
        obj = Doubts.objects.get(doubt_id=idd)
        obj.reply = request.POST.get('reply')
        obj.save()
        return view_doubt_post_reply(request)
    return render(request, 'doubts/reply.html')

def view_doubt_post_reply(request):
    obj=Doubts.objects.all()
    context={
        'a':obj
    }
    return render(request, 'doubts/view_doubt_post_reply.html',context)

def view_doubt_reply(request):
    ss=request.session["u_id"]
    obj=Doubts.objects.filter(student_id=ss)
    context={
        'b':obj
    }
    return render(request,'doubts/viewDoubtsReply.html',context)

