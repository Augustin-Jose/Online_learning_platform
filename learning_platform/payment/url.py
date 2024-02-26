from django.conf.urls import url
from payment import views

urlpatterns = [
    url('pay/(?P<idd>\w+)', views.pay),
    url('payment_details/', views.paymentDetails),
    url('approved/(?P<idd>\w+)', views.approve),
    url('rejected/(?P<idd>\w+)', views.reject),
    url('payedcourse/', views.payedcourse),

]