from django.urls import path
from banner import views


urlpatterns=[
    
    path('post_banner/',views.post_banner),
    path('view_banner/',views.view_banner),
   
]
