from django.shortcuts import render
from django.http import JsonResponse
from page.models import Page
import datetime
# Create your views here.

def post_page(request):
    if request.method == 'POST':
        obj=Page()
        obj.meta_title=request.POST.get('metatitle')
        obj.image=request.POST.get('image')
        obj.title=request.POST.get('title')
        obj.priority=request.POST.get('priority')
        obj.meta_description=request.POST.get('metadescription')
        obj.page_name=request.POST.get('pagename')
        obj.url=request.POST.get('url')
        obj.heading=request.POST.get('heading')
        obj.description=request.POST.get('description')
        obj.category=request.POST.get('category')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request,'page/post_page.html')

def view_page(request):
    obj=Page.objects.all()
    context={
        'x':obj
    }
    return render(request,'page/view_page.html',context)





