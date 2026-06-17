from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_profile, name="create_profile"),
    path("my-profile/", views.my_profile, name="my_profile"),
    path("edit/", views.edit_profile, name="edit_profile"),
    path("delete/", views.delete_profile, name="delete_profile"),
]