from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_profile, name="create_profile"),
    path("my-profile/", views.my_profile, name="my_profile"),
    path("edit/", views.edit_profile, name="edit_profile"),
    path("delete/", views.delete_profile, name="delete_profile"),
    path("skills/", views.my_skills, name="my_skills"),
path("skills/add/", views.add_skill, name="add_skill"),
path("skills/delete/<int:pk>/", views.delete_skill, name="delete_skill"),
path("skills/edit/<int:pk>/", views.edit_skill, name="edit_skill"),
]