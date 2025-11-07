from django.shortcuts import render
from contact.models import Contact
import datetime

from team.models import Team  # Model names are Capitalized by convention

def about(request):
    # Get all team members from the database
    obj = Team.objects.all().order_by('priority')
    
    # Pass them to the template context
    context = {
        'x': obj
    }
    
    # Render the 'about' page template
    return render(request, 'temp/about.html', context)

def base(request):
    return render(request, 'temp/base.html')

def contact(request):
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

def gallery(request):
    return render(request,'temp/gallery.html')

def index(request):
    return render(request, 'temp/index.html')

def project(request):
    return render(request,'temp/project.html')

def service(request):
    return render(request, 'temp/service.html')

def testimonial(request):
    return render(request,'temp/testimonial.html')

def admin(request):
    return render(request,'temp/admin.html')






# Create your views here.
