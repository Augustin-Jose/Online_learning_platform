from django.shortcuts import render
from tutorial.models import Tutorial



def classes(request):
    if request.method == 'POST':
        obj = Tutorial()
        obj.video = request.POST.get('video')
        obj.notes = request.POST.get('notes')
        obj.subject= request.POST.get('subject')
        obj.teacher_id = 1
        obj.save()
    return render(request, 'tutorial/classes.html')

def view_class(request):
    return render(request,'tutorial/viewclass.html')