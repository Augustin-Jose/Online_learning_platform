from django.conf.urls import url
from payment import views

urlpatterns = [
    url('payment/',views.payment),
    url('payment_details/',views.paymentDetails),

]