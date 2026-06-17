from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_roadmaps, name="my_roadmaps"),
    path("create/", views.create_roadmap, name="create_roadmap"),
]