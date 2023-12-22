from django.conf.urls import url
from teacher import views

urlpatterns = [
    url('teacher/',views.teacher),
    url('adm_tea/',views.adm_man_teacher),
    url('approve/(?P<idd>\w+)', views.approve),
    url('reject/(?P<idd>\w+)', views.reject),

]