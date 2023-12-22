from django.conf.urls import url
from progress import views

urlpatterns = [
    url('progress/',views.progress),
    url('view/',views.view_progress),

]