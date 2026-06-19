from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_roadmaps, name="my_roadmaps"),
    path("create/", views.create_roadmap, name="create_roadmap"),
    path("<int:pk>/", views.roadmap_detail, name="roadmap_detail"),
    
    path("<int:roadmap_id>/milestone/add/", views.add_milestone, name="add_milestone"),
path("milestone/<int:pk>/edit/", views.edit_milestone, name="edit_milestone"),
path("milestone/<int:pk>/delete/", views.delete_milestone, name="delete_milestone"),

path("milestone/<int:milestone_id>/task/add/", views.add_task, name="add_task"),
path("task/<int:pk>/toggle/", views.toggle_task, name="toggle_task"),
path("task/<int:pk>/delete/", views.delete_task, name="delete_task"),
path("task/<int:pk>/edit/", views.edit_task, name="edit_task"),

path("<int:pk>/edit/", views.edit_roadmap, name="edit_roadmap"),
path("<int:pk>/delete/", views.delete_roadmap, name="delete_roadmap"),

path("<int:roadmap_id>/course/add/", views.add_course, name="add_course"),
path("course/<int:pk>/edit/", views.edit_course, name="edit_course"),
path("course/<int:pk>/delete/", views.delete_course, name="delete_course"),

path("<int:roadmap_id>/project/add/", views.add_project, name="add_project"),
path("project/<int:pk>/edit/", views.edit_project, name="edit_project"),
path("project/<int:pk>/delete/", views.delete_project, name="delete_project"),

path("course/<int:pk>/toggle/", views.toggle_course, name="toggle_course"),
path("project/<int:pk>/toggle/", views.toggle_project, name="toggle_project"),
]