from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from .filters import UserFilter
from django.urls import reverse
from .forms import AuthForm
from django.core.paginator import Paginator 

 
# Create your views here.
class Logout(LoginRequiredMixin, LogoutView):
    next_page = "login"
    login_url = "login"


class Login(LoginView):
    template_name = "users/auth.html"
    authentication_form = AuthForm
    next_page="home"
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse("home")

    def form_invalid(self, form: AuthForm):
        return super().form_invalid(form)


@login_required(login_url="login")
def view_all_users(request):
    filter_users = UserFilter(request.GET, queryset=User.objects.filter(deleted__isnull=True))
    paginator = Paginator(filter_users.qs,1) #20
    if request.GET.get("page"):
        page_num = request.GET.get("page")
    else:
        page_num = 1
    users = paginator.page(page_num)
    context = {"users": users, "filter_users": filter_users}
    return render(request, "users/users.html", context)
