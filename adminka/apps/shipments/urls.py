from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_all_shipments, name="view-shipments"),
    path("create", views.create_shipment, name="create-shipment"),
    path("<int:pk>", views.view_shipment, name="view-shipment"),
    path("<int:pk>/update", views.update_shipment, name="update-shipment"),
    path("<int:pk>/delete", views.delete_shipment, name="delete-shipment"),
]
