from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, Permission
from .forms import ViewGroup, GroupForm
from ..notifications.models import Notification
from django.utils import timezone


# Create your views here.
def not_found_view(request, exception):
    return render(request, "error.html")


@login_required(login_url="login")
def index(request):
    now = timezone.now()
    notifications = Notification.objects.filter(end__gt=now).order_by("start")
    context = {"notifications": notifications}
    return render(request, "index.html", context)


@login_required(login_url="login")
@permission_required("groups.view_group")
def view_all_groups(request):
    groups = Group.objects.all()
    context = {"groups": groups}
    return render(request, "base/groups.html", context)


@login_required(login_url="login")
@permission_required("groups.view_group")
def view_group(request, pk):
    group = Group.objects.get(id=pk)
    form = ViewGroup(instance=group)
    permissions = group.permissions.all()
    context = {"group": group, "permissions": permissions, "form": form}
    return render(request, "base/view-group.html", context)


@login_required(login_url="login")
@permission_required("groups.add_group")
def create_group(request):
    form = GroupForm()
    context = {"form": form}
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect("view-groups")
    return render(request, "base/create-group.html", context)


@login_required(login_url="login")
@permission_required("groups.change_group")
def update_group(request, pk):
    group = Group.objects.get(id=pk)
    permissions = group.permissions.all()
    form = GroupForm(instance=group)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        group = form.save()
        group.save()
        return redirect("view-group", group.id)
    context = {
        "group": group,
        "permissions": permissions,
        "form": form,
    }
    return render(request, "base/update-group.html", context)


@login_required(login_url="login")
@permission_required("groups.delete_group")
def delete_group(request, pk):
    group = Group.objects.get(id=pk)
    group.delete()
    return redirect("view-groups")


@login_required(login_url="login")
@permission_required("groups.change_group")
def update_group_permissions(request, pk):
    group = Group.objects.get(id=pk)
    group_permissions = group.permissions.all()
    permissions = Permission.objects.exclude(group__id=group.id)
    context = {
        "group": group,
        "group_permissions": group_permissions,
        "permissions": permissions,
    }
    return render(request, "base/update-group-permissions.html", context)


@login_required(login_url="login")
@permission_required("groups.change_group")
def add_group_permission(request, pk, perm_id):
    group = Group.objects.get(id=pk)
    group.permissions.add(perm_id)
    return redirect("update-group-permissions", pk)


@login_required(login_url="login")
@permission_required("groups.change_group")
def remove_group_permission(request, pk, perm_id):
    group = Group.objects.get(id=pk)
    group.permissions.remove(perm_id)
    return redirect("update-group-permissions", pk)
