from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .filters import UserFilter

# Create your views here.
class Logout(LoginRequiredMixin, LogoutView):
    next_page = "home"
    #login_url = "login"

def view_all_users(request):
    users = UserFilter(request.GET, queryset=User.objects.filter(deleted__isnull=True))
    #users = User.objects.filter(deleted__isnull=True)
    context = {"users": users}
    return render(request, "users/users.html", context)