from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UsersList.as_view(), name='api-users'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='api-user'),
    path('users/<int:pk>/groups', views.UserDetailsGroups.as_view(), name='api-user-groups'),
]

urlpatterns = format_suffix_patterns(urlpatterns)