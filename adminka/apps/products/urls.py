from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_all_products, name="view-products"),
    path("create", views.create_product, name="create-product"),
    path("<int:pk>", views.view_products, name="view-product"),
    path("<int:pk>/update", views.update_product, name="update-product"),
    path("<int:pk>/delete", views.delete_product, name="delete-product"),
    path("<int:pk>/update/image/<int:img_id>", views.delete_product_image, name="delete-product-image"),
]