from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("groups", views.view_all_groups, name="view-groups"),
    path("groups/create", views.create_group, name="create-group"),
    path("groups/<int:pk>", views.view_group, name="view-group"),
    path("groups/<int:pk>/update", views.update_group, name="update-group"),
    path("groups/<int:pk>/delete", views.delete_group, name="delete-group"),
    path("groups/<int:pk>/update/permissions", views.update_group_permissions, name="update-group-permissions"),
    path("groups/<int:pk>/update/permissions/add/<int:perm_id>", views.add_group_permission, name="add-group-permission"),
    path("groups/<int:pk>/update/permissions/remove/<int:perm_id>", views.remove_group_permission, name="remove-group-permission"),
]
