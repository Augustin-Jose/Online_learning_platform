from django.conf.urls import url
from teacher import views

urlpatterns = [url('teacher/',views.teacher),

url('add_teacher/',views.add_teacher),

url('adm_man_teacher/',views.adm_man_teacher),

]