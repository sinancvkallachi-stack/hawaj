from django.shortcuts import render,redirect
from gallery.models import Gallery
import datetime
# Create your views here.

def post_gallery(request):
    if request.method == 'POST':
        obj=Gallery()
        obj.category=request.POST.get('category')
        obj.image=request.FILES.get('image')
        obj.title=request.POST.get('title')
        obj.priority=request.POST.get('priority')
        obj.condition=request.POST.get('condition')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request,'gallery/post_gallery.html')

def view_gallery(request):
    obj = Gallery.objects.all().order_by('priority')

    
    
    context={
        'x':obj
    }
    return render(request,'gallery/view_gallery.html',context)

