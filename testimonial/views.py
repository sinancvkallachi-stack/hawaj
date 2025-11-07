from django.shortcuts import render
from testimonial.models import Testimonial
import datetime
# Create your views here.

def post_testimonial(request):
    if request.method == 'POST':
        obj=Testimonial()
        obj.name=request.POST.get('name')
        obj.role=request.POST.get('role')
        obj.testimonial=request.POST.get('testimonial')
        obj.category=request.POST.get('category')
        obj.priority=request.POST.get('priority')
        obj.condition=request.POST.get('condition')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request,'testimonial/post_testimonial.html')

def view_testimonial(request):
    obj=Testimonial.objects.all()
    context={
        'x':obj
    }
    return render(request,'testimonial/view_testimonial.html',context)
