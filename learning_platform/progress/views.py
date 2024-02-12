from django.shortcuts import render
from progress.models import Progress
from course.models import  Course
from student.models import Student
def progress(request):
    ss=request.session["u_id"]
    ob=Course.objects.all()
    on=Student.objects.all()
    contwxt={
        'x':ob,
        'y':on
    }
    if request.method == 'POST':
        obj = Progress()
        obj.course_id = request.POST.get('course')
        obj.progress = request.POST.get('progress')
        obj.teacher_id = ss
        obj.student_id = request.POST.get('student')
        obj.save()
    return render(request,'progress/progess.html',contwxt)


def view_progress(request):
    ss= request.session["u_id"]
    obj=Progress.objects.filter(student_id=ss)
    context={
        'a':obj
    }
    return render(request,'progress/viewProgess.html',context)


