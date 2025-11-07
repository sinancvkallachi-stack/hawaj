from django.urls import path
from page import views


urlpatterns=[
    
    path('post_page/',views.post_page),
    path('view_page/',views.view_page),
    
]