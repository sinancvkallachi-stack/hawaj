from django.urls import path
from gallery import views


urlpatterns=[
    
    path('post_gallery/',views.post_gallery),
    path('view_gallery/',views.view_gallery),
   
]