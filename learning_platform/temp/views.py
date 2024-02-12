from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'temp/about.html')

def admin(request):
    return render(request, 'temp/admin.html')

def contact(request):
    return render(request, 'temp/contact.html')

def courses(request):
    return render(request, 'temp/courses.html')

def index(request):
    return render(request, 'temp/index.html')

def student_home(request):
    return render(request, 'temp/student_home.html')

def teacher_home(request):
    return render(request, 'temp/teacher_home.html')

def index2(request):
    return render(request, 'temp/index2.html')

def  student2(request):
    return render(request, 'temp/student2.html')
def  about2(request):
    return render(request, 'temp/about2.html')

def  contact2(request):
    return render(request, 'temp/contact2.html')

def  courses2(request):
    return render(request, 'temp/courses2.html')

def  about3(request):
    return render(request, 'temp/about3.html')


def  contact3(request):
    return render(request, 'temp/contact3.html')