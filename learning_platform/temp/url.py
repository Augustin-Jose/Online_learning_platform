from django.conf.urls import url
from temp import views


urlpatterns=[
    url('about/', views.about),
    url('admin/', views.admin),
    url('contact/', views.contact),
    url('courses/', views.courses),
    url('index/', views.index),
    url('student_home', views.student_home),
    url('teacher_home/', views.teacher_home),
    url('index2/', views.index2),
    url('student2/',views.student2),
    url('about2/',views.about2),
    url('contact2/',views.contact2),
    url('courses2/', views.courses2),
    url('about3/', views.about3),
    url('contact3/', views.contact3),

]