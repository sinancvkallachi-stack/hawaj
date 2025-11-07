from django.urls import path
from testimonial import views


urlpatterns=[
    
    path('post_testimonial/',views.post_testimonial),
    path('view_testimonial/',views.view_testimonial),
    
]