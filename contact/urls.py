from django.urls import path
from contact import views


urlpatterns=[
    
    path('post_contact/',views.post_contact),
    path('view_contact/',views.view_contact),
    
]