from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_roadmaps, name="my_roadmaps"),
    path("create/", views.create_roadmap, name="create_roadmap"),
    path("<int:pk>/", views.roadmap_detail, name="roadmap_detail"),
    
    path("<int:roadmap_id>/milestone/add/", views.add_milestone, name="add_milestone"),
path("milestone/<int:pk>/edit/", views.edit_milestone, name="edit_milestone"),
path("milestone/<int:pk>/delete/", views.delete_milestone, name="delete_milestone"),
]