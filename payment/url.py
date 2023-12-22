from django.conf.urls import url
from payment import views

urlpatterns = [
<<<<<<< HEAD
    url('payment/(?P<idd>\w+)',views.payment),
=======
    url('payment/',views.payment),
>>>>>>> c1edbc4fc6a75406916eeeae4b4d0b2b2164d7ce
    url('payment_details/',views.paymentDetails),
    url('approved/(?P<idd>\w+)',views.approve),
    url('rejected/(?P<idd>\w+)',views.reject),

]