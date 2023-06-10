from django.urls import path
from . import views


urlpatterns = [
    path("logout/", views.Logout.as_view(),name="logout"),
    path("users/", views.view_all_users, name="view-users"),
    #path("user/<int:pk>", name="view-user"),
    #path("user/delete/<int:pk>", name="delete-user"),
    #path("user/update/<int:pk>", name="update-user"),
]
