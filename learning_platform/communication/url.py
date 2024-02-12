from django.conf.urls import url
from communication import views

urlpatterns = [
    url('communication/',views.communication),
    url('view_communication',views.view_communication),
]