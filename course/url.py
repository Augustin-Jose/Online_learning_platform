from django.conf.urls import url
from course import views


urlpatterns = [
    url('course/',views.course),

    url('view/',views.view_course),

    url('course_pay/',views.course_pay),


]