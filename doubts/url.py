from django.conf.urls import url
from doubts import views

urlpatterns = [
    url('doubts/',views.doubts),

<<<<<<< HEAD
    url('reply/(?P<idd>\w+)',views.reply),
=======
    url('reply/',views.reply),
>>>>>>> c1edbc4fc6a75406916eeeae4b4d0b2b2164d7ce

    url('doubt_post/',views.view_doubt_post_reply),

    url('doubt_reply/',views.view_doubt_reply),



]