from django.shortcuts import render ,get_object_or_404, redirect
from team.models import Team
from django import forms
import datetime

# class TeamForm(forms.ModelForm):
#     class Meta:
#         model = Team
#         fields = ['name', 'role', 'priority', 'image']
        
# Create your views here.

def post_team(request):
    if request.method == 'POST':
        obj=Team()
        obj.name=request.POST.get('name')
        obj.image=request.FILES.get('image')
        obj.category=request.POST.get('category')
        obj.instagram=request.POST.get('instagram')
        obj.facebook=request.POST.get('facebook')
        obj.linkedin=request.POST.get('linkedin')
        obj.role=request.POST.get('role')
        obj.priority=request.POST.get('priority')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request,'team/post_team.html')

def view_team(request):
   obj = Team.objects.all().order_by('priority')
   context={
        'x':obj
    }
   return render(request,'team/view_team.html',context)


def edit_team(request, team_id):
    # Get the existing team object
    item = get_object_or_404(Team, pk=team_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        priority = request.POST.get('priority')

        # Validate all fields
        if not name or not role or not priority:
            return render(request, 'team/team_form.html', {
                'item': item,
                'error': 'All fields are required!'
            })

        # Update fields
        item.name = name
        item.role = role
        item.priority = priority

        # Update image only if uploaded
        if 'image' in request.FILES:
            item.image = request.FILES['image']

        # Update timestamps (optional)
        item.date = datetime.date.today()
        item.time = datetime.datetime.now().time()

        item.save()
        return redirect('view_team')  # redirect to your list page

    # GET request: show the form with existing data
    return render(request, 'team/post_team.html', {'item': item})
# def add_team(request):
#     if request.method == "POST":
#         form = TeamForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('view_team')
#     else:
#         form = TeamForm()

#     return render(request, 'team_form.html', {'form': form})






