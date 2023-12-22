from django.shortcuts import render
from course.models import Course
# Create your views here.

def course(request):
    if request.method == 'POST':
        obj = Course()
        obj.course = request.POST.get('course')
        obj.course_fee = request.POST.get('fee')
        obj.duration = request.POST.get('duration')
        obj.save()
    return render(request,'course/course.html')

def course_pay(request):
    obj=Course.objects.all()
    context={
        'a':obj
    }
    return render(request,'course/view_course_pay.html',context)

def view_course(request):
    obj=Course.objects.all()
    context={
        'b':obj
    }
    return render(request,'course/viewcourse.html',context)

