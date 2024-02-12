from django.conf.urls import url
from student import views

urlpatterns = [
    url('student/', views.student),
    url('admin_man_user/', views.admin_man_user),
    url('ad_v_stud/', views.ad_v_stud),
    url('edit/(?P<idd>\w+)', views.edit),
    url('delete/(?P<idd>\w+)', views.delete),
    # url('edit_student/(?P<idd>\w+)', views.student_edit),
    url('edit_profile/(?P<idd>\w+)',views.student_edit)

]