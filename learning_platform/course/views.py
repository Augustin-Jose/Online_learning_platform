from django.shortcuts import render
from course.models import Course
from course.models import Quiz
import datetime
from django.core.files.storage import FileSystemStorage
# Create your views here.

def course(request):
    if request.method == 'POST':
        obj = Course()
        obj.course = request.POST.get('course')
        obj.description = request.POST.get('description')
        obj.course_fee = request.POST.get('fee')
        obj.duration = request.POST.get('duration')
        obj.save()
    return render(request,'course/course.html')

def course_pay(request):
    obj=Course.objects.all()
    context={
        'c':obj
    }
    return render(request,'course/view_course_pay.html',context)

def view_course(request):
    obj=Course.objects.all()
    context={
        'b':obj
    }
    return render(request,'course/viewcourse.html',context)

def webdevelopment(request):
    obj=Course.objects.all()
    context={
        'b':obj
    }
    return render(request,'course/webdevelopment.html',context)

def python_fundamental(request):
    obj=Course.objects.all()
    context={
        'b':obj
    }
    return render(request,'course/python_fundamental.html',context)

def java_programming_essentials(request):
    obj=Course.objects.all()
    context={
        'b':obj
    }
    return render(request,'course/java_programming_essentials.html',context)

def machine_learning_basics(request):
    obj=Course.objects.all()
    context={
        'b':obj
    }
    return render(request, 'course/machine_learning_basics.html', context)

def frontend_development_with_react(request):
    obj=Course.objects.all()
    context={
        'b':obj
    }
    return render(request, 'course/frontend_development_with_react.html', context)

def cybersecurity_fundamentals  (request):
    obj=Course.objects.all()
    context={
        'b':obj
    }
    return render(request, 'course/cybersecuurity_fundamental.html', context)

def data_science (request):
    obj=Course.objects.all()
    context={
        'b':obj
    }
    return render(request, 'course/dataScience.html', context)

def cloud_computing(request):
    obj=Course.objects.all()
    context={
        'b':obj
    }
    return render(request, 'course/Cloud computing.html', context)

def Free_courses  (request):
    obj=Course.objects.all()
    context={
        'b':obj
    }
    return render(request, 'course/Free_courses.html', context)

def sql  (request):
    obj=Course.objects.all()
    context={
        'b':obj
    }
    return render(request, 'course/sql.html', context)

def quiz(request):
    ss = request.session["u_id"]
    if request.method =='POST':
        obj=Quiz()
        obj.teacher_id = ss
        obj.student_id=1
        obj.quiz = request.POST.get('quiz')
        obj.date = datetime.datetime.today()
        obj.upload = 'pending'
        obj.save()
    return render(request, 'course/add_quiz.html')


def view_quiz(request):
    obj = Quiz.objects.all()
    context = {
        'a': obj
    }
    return render(request, 'course/view_quiz.html',context)

def upload(request,idd):
    ss=request.session["u_id"]
    if request.method=='POST':
        obj=Quiz.objects.get(quiz_id=idd)
        myfile=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.upload=myfile.name
        obj.student_id=ss
        obj.save()
    return render(request,'course/upload.html')

def view_quiz_ans(request):
    obj=Quiz.objects.all()
    context={
        'x':obj
    }
    return render(request,'course/view_quiz_ans.html',context)

