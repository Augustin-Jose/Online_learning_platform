from django.conf.urls import url
from student import views

urlpatterns = [
    url('student/', views.student),
    url('admin_man_user/', views.admin_man_user),
    url('edit/(?P<idd>\w+)', views.edit),
    url('delete/(?P<idd>\w+)', views.delete),
<<<<<<< HEAD
    # url('edit_student/(?P<idd>\w+)', views.student_edit),
    url('edit_profile/(?P<idd>\w+)',views.student_edit)
=======
    url(r'^edit_student/(?P<idd>\w+)/$', views.student_edit),
>>>>>>> c1edbc4fc6a75406916eeeae4b4d0b2b2164d7ce

]