from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_all_notifications, name="view-notifications"),
    path("<int:pk>", views.view_notification, name="view-notification"),
    path("create", views.create_notification, name="create-notification"),
    path("<int:pk>/update", views.update_notification, name="update-notification"),
    path("<int:pk>/delete", views.delete_notification, name="delete-notification"),
]
