from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from .filters import UserFilter
from django.urls import reverse
from .forms import AuthForm
from django.core.paginator import Paginator
from .forms import UserUpdateForm
from django.utils import timezone

# Create your views here.
class Logout(LoginRequiredMixin, LogoutView):
    next_page = "login"
    login_url = "login"


class Login(LoginView):
    template_name = "users/auth.html"
    authentication_form = AuthForm
    next_page = "home"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse("home")

    def form_invalid(self, form: AuthForm):
        return super().form_invalid(form)


@login_required(login_url="login")
def view_all_users(request):
    filter_users = UserFilter(
        request.GET, queryset=User.objects.filter(deleted__isnull=True)
    )
    paginator = Paginator(filter_users.qs, 20)
    if request.GET.get("page"):
        page_num = request.GET.get("page")
    else:
        page_num = 1
    users = paginator.page(page_num)
    context = {"users": users, "filter_users": filter_users}
    return render(request, "users/users.html", context)


@login_required(login_url="login")
def view_user(request, pk):
    user = User.objects.get(id=pk)
    groups = user.groups.all()
    context = {"user": user, "groups": groups}
    return render(request, "users/view-user.html", context)


@login_required(login_url="login")
def update_user(request, pk):
    user = User.objects.get(id=pk)
    form = UserUpdateForm(instance=user)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect("view-user", user.id)
    context = {"user": user, "form": form}
    return render(request, "users/update-user.html", context)

@login_required(login_url="login")
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.deleted = timezone.now()
    user.is_active = False
    user.save()
    return redirect("view-users")