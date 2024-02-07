from django.conf.urls import url
from course import views


urlpatterns = [
    url('course/',views.course),

    url('view/',views.view_course),

    url('course_pay/',views.course_pay),

    url('web_development/', views.webdevelopment),

    url('python_fundamental/', views.python_fundamental),

    url('java_programming_essentials/', views.java_programming_essentials),

    url('machine_learning_basics/', views.machine_learning_basics),

    url('frontend_development_with_react/', views.frontend_development_with_react),

    url('cybersecurity_fundamentals/', views.cybersecurity_fundamentals),

]