from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from tutorial.models import Tutorial
from django.views.static import serve


def classes(request):
    ss= request.session["u_id"]
    if request.method == 'POST':
        obj = Tutorial()
        obj.video = request.POST.get('video')
        # myfile=request.FILES['video']
        # fs=FileSystemStorage()
        # filename=fs.save(myfile.name,myfile)
        # obj.video = myfile.name

        # obj.notes = request.POST.get('notes')
        myfile = request.FILES['notes']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.notes = myfile.name

        obj.subject= request.POST.get('subject')
        obj.teacher_id = ss
        obj.save()
    return render(request, 'tutorial/classes.html')

def view_class(request):
    obj=Tutorial.objects.all()
    context={
        'a':obj
    }
    return render(request,'tutorial/viewclass.html',context)


