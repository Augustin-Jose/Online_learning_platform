from django.shortcuts import render
from payment.models import Payment
from course.models import Course
import datetime
def payment(request,idd):
    obj1 = Course.objects.get(course_id=idd)
    context = {
        'a': obj1
    }
    if request.method == 'POST':
        obj = Payment()
        obj.username = request.POST.get('username')
        obj.payment_method = request.POST.get('payment_method')
        obj.amount = request.POST.get('amount')
        obj.status = 'pending'
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.save()
    return render(request,'payment/payment.html',context)

def paymentDetails(request):
    obj = Payment.objects.all()
    context = {
        'a' : obj
    }
    return render(request, 'payment/paymentDetails.html',context)
def approve(request,idd):
    obj=Payment.objects.get(payment_id=idd)
    obj.status='approve'
    obj.save()
    return paymentDetails(request)

def reject(request, idd):
    obj = Payment.objects.get(payment_id=idd)
    obj.status = 'reject'
    obj.save()
    return paymentDetails(request)



