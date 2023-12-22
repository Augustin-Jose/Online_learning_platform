from django.shortcuts import render
from progress.models import Progress

def progress(request):
    if request.method == 'POST':
        obj = Progress()

        obj.course_id = 1

        obj.progress = request.POST.get('progress')

        obj.teacher_id = 1
        obj.student_id = 1

        obj.save()
    return render(request,'progress/progess.html')


def view_progress(request):
    obj=Progress.objects.all()
    context={
        'a':obj
    }
    return render(request,'progress/viewProgess.html',context)


