from django.urls import path
from temp import views
from temp.views import index,about,base,gallery,contact,project,service,testimonial

urlpatterns=[
    path('about.html/',views.about),
    path('base.html/',views.base),
    path('contact.html/',views.contact),
    path('gallery.html/',views.gallery),
    path('index.html/',views.index),
    path('project.html/',views.project),
    path('service.html/',views.service),
    path('testimonial.html/',views.testimonial),
    path('admin.html/',views.admin),




]
