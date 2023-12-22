from django.conf.urls import url
from doubts import views

urlpatterns = [
    url('doubts/',views.doubts),

    url('reply/(?P<idd>\w+)',views.reply),

    url('doubt_post/',views.view_doubt_post_reply),

    url('doubt_reply/',views.view_doubt_reply),



]