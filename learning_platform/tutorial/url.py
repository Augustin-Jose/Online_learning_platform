from django.conf.urls import url
from tutorial import views
urlpatterns = [
    url('classes/',views.classes),
    url('view_clas/',views.view_class),

]