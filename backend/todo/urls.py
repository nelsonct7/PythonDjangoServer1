from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="todo-list"),
    path("create", views.create_todo, name="create"),
    path("edit/<pk>", views.edit_todo, name="edit"),
    path("delete/<pk>", views.delete_todo, name="delete"),
]