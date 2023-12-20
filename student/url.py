from django.conf.urls import url
from student import views

urlpatterns = [
    url('student/',views.student),
    url('admin_man_user/',views.admin_man_user),
    url('edit/(?P<idd>\w+)',views.edit),
    url('delete/(?P<idd>\w+)', views.delete),
    url('aaaaa/(?P<idd>\w+)', views. student_edit),

]