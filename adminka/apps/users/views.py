from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth import logout
from .models import User
from .filters import UserFilter
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import UserUpdateForm, UserCreateForm, AuthForm, ViewUser
from django.utils import timezone
from .services import create_user_emailing
import secrets


# Create your views here.
# class Logout(LoginRequiredMixin, LogoutView):
#     next_page = "login"
#     login_url = "login"


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect("login")


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
@permission_required("users.view_user", login_url="login")
def view_all_users(request):
    filter = UserFilter(
        request.GET, queryset=User.objects.filter(deleted__isnull=True).order_by("id")
    )
    paginator = Paginator(filter.qs, 20)
    if request.GET.get("page"):
        page_num = request.GET.get("page")
    else:
        page_num = 1
    users = paginator.page(page_num)
    context = {"users": users, "filter": filter}
    return render(request, "users/users.html", context)


@login_required(login_url="login")
@permission_required("users.view_user", login_url="login")
def view_user(request, pk):
    user = User.objects.get(id=pk)
    form = ViewUser(instance=user)
    groups = user.groups.all()
    context = {"user": user, "groups": groups, "form": form}
    return render(request, "users/view-user.html", context)


@login_required(login_url="login")
@permission_required("users.change_user", login_url="login")
def update_user(request, pk):
    user = User.objects.get(id=pk)
    groups = user.groups.all()
    form = UserUpdateForm(instance=user, use_required_attribute=False)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect("view-user", user.id)
    context = {"user": user, "form": form, "groups": groups}
    return render(request, "users/update-user.html", context)


@login_required(login_url="login")
@permission_required("users.delete_user", login_url="login")
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect("view-users")


@login_required(login_url="login")
@permission_required("users.add_user", login_url="login")
def create_user(request):
    form = UserCreateForm()
    context = {"form": form}
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = secrets.token_hex()
            user.set_password(password)
            user.save()
            create_user_emailing(user.email, password)
            return redirect("view-users")
    return render(request, "users/create-user.html", context)


@login_required(login_url="login")
@permission_required("users.change_user", login_url="login")
def update_user_groups(request, pk):
    user = User.objects.get(id=pk)
    user_groups = user.groups.all()
    all_groups = Group.objects.exclude(user__id=user.id)
    context = {"user": user, "user_groups": user_groups, "groups": all_groups}
    return render(request, "users/update-user-groups.html", context)


@login_required(login_url="login")
@permission_required("users.change_user", login_url="login")
def remove_user_group(request, pk, gr_id):
    user = User.objects.get(id=pk)
    user.groups.add(gr_id)
    return redirect("update-user-groups", pk)


@login_required(login_url="login")
@permission_required("users.change_user", login_url="login")
def add_user_group(request, pk, gr_id):
    user = User.objects.get(id=pk)
    user.groups.remove(gr_id)
    return redirect("update-user-groups", pk)


@login_required(login_url="login")
def user_settings(request):
    user = request.user
    general_form = UserUpdateForm(instance=user, use_required_attribute=False)
    if request.method == "POST":
        if "conf_gen" in request.POST:
            general_form = UserUpdateForm(
                request.POST, instance=user, use_required_attribute=False
            )
            if general_form.is_valid():
                user = general_form.save()
        elif "conf_pass" in request.POST:
            if request.POST.get("pass1"):
                if request.POST.get("pass1") == request.POST.get("pass2"):
                    user.set_password(request.POST.get("pass2"))
                    user.save()
    context = {"user": user, "general_form": general_form}
    return render(request, "users/user-settings.html", context)
