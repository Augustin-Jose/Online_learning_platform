from django.shortcuts import render
from communication.models import Communication
# Create your views here.

def communication(request):
    if request.method == 'POST':
        obj = Communication()
        obj.notification = request.POST.get('notification')
        obj.date = request.POST.get('date')
        obj.time = request.POST.get('time')
        obj.save()
    return render(request, 'communication/communication.html')

def view_communication(request):
    obj=Communication.objects.all()
    context = {
        'b': obj
    }
    return render(request, 'communication/view_communication.html',context)