from django.conf.urls import url
from payment import views

urlpatterns = [
    url('payment/',views.payment),
    url('payment_details/',views.paymentDetails),
    url('approved/(?P<idd>\w+)',views.approve),
    url('rejected/(?P<idd>\w+)',views.reject),

]