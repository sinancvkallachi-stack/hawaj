from django.urls import path
from project import views


urlpatterns=[
    
    path('post_project/',views.post_project),
    path('view_project/',views.view_project),
    
]