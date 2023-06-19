from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_all_tags, name="view-tags"),
    path("create", views.create_tag, name="create-tag"),
    path("<int:pk>", views.view_tag, name="view-tag"),
    path("<int:pk>/delete", views.delete_tag, name="delete-tag"),
    path("<int:pk>/update", views.update_tag, name="update-tag"),
]
