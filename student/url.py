from django.conf.urls import url
from student import views

urlpatterns = [url('student/',views.student),

url('admin_man_user/',views.admin_man_user),

]