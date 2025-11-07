from django.shortcuts import render
from project.models import Project
import datetime
# Create your views here.

def post_project(request):
    if request.method == 'POST':
        obj=Project()
        obj.category=request.POST.get('category')
        obj.image=request.POST.get('image')
        obj.youtubelink = request.POST.get('youtube')
        obj.priority=request.POST.get('priority')
        obj.feature=request.POST.get('feature')
        obj.condition=request.POST.get('condition')
        obj.heading=request.POST.get('heading')
        obj.description=request.POST.get('description')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request,'project/post_project.html')

def view_project(request):
    obj=Project.objects.all()
    context={
        'x':obj
    }
    return render(request,'project/view_project.html',context)
