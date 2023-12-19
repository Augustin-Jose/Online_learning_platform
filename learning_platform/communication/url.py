from django.conf.urls import url
from communication import views

urlpatterns = [
url('communication/',views.communication),
]