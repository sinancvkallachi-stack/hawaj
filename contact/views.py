from django.shortcuts import render
from contact.models import Contact
import datetime
# Create your views here.

def post_contact(request):
    if request.method == 'POST':
        obj=Contact()
        obj.name=request.POST.get('name')
        obj.number=request.POST.get('number')
        obj.email=request.POST.get('email')
        obj.message=request.POST.get('message')
        obj.category=request.POST.get('category')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request,'temp/contact.html')

def view_contact(request):
    obj=Contact.objects.all()
    context={
        'x':obj
    }
    return render(request,'contact/view_contact.html',context)
