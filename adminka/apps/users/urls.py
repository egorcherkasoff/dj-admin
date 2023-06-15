from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(),name="logout"),
    path("settings/", views.user_settings, name="user-settings"),
    path("users/", views.view_all_users, name="view-users"),
    path("users/create", views.create_user, name="create-user"),
    path("users/<int:pk>", views.view_user, name="view-user"),
    path("users/<int:pk>/delete", views.delete_user, name="delete-user"),
    path("users/<int:pk>/update", views.update_user, name="update-user"),
    path("users/<int:pk>/update/groups", views.update_user_groups, name="update-user-groups"),
    path("users/<int:pk>/update/groups/add/<int:gr_id>", views.add_user_group, name="remove-user-group"),
    path("users/<int:pk>/update/groups/remove/<int:gr_id>", views.remove_user_group, name="add-user-group"),
]
