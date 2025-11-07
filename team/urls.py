from django.urls import path
from team import views

urlpatterns=[
    path('post_team/', views.post_team),
    path('view_team/', views.view_team),
    path('edit/<int:team_id>/', views.edit_team, name='edit_team'),
    # path('add/', views.add_team, name='add_team'),
]


