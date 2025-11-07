from django.shortcuts import render
from banner.models import Banner
import datetime
# Create your views here.

def post_banner(request):
    if request.method == 'POST':
        obj=Banner()
        obj.image=request.POST.get('image')
        obj.heading=request.POST.get('heading')
        obj.description=request.POST.get('description')
        obj.category=request.POST.get('category')
        obj.priority=request.POST.get('priority')
        obj.condition=request.POST.get('condition')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request,'banner/post_banner.html')

def view_banner(request):
    obj = Banner.objects.all().order_by('priority')
    
    context={
        'x':obj
    }
    return render(request,'banner/view_banner.html',context)


