from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Notification
from .filters import NotificationFilter
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import NotificationForm, ViewNotification
from django.utils import timezone

# Create your views here.
@login_required(login_url="login")
@permission_required("notifications.view_notification", login_url="login")
def view_all_notifications(request):
    filter = NotificationFilter(
        request.GET, queryset=Notification.objects.filter(deleted__isnull=True).order_by("end")
    )
    paginator = Paginator(filter.qs, 20)
    if request.GET.get("page"):
        page_num = request.GET.get("page")
    else:
        page_num = 1
    notifications = paginator.page(page_num)
    context = {"notifications": notifications, "filter": filter}
    return render(request, "notifications/notifications.html", context)


@login_required(login_url="login")
@permission_required("notifications.view_notification", login_url="login")
def view_notification(request, pk):
    notification = Notification.objects.get(id=pk)
    form = ViewNotification(instance=notification)
    context = {"notification": notification, "form":form}
    return render(request, "notifications/view-notification.html", context)


@login_required(login_url="login")
@permission_required("notifications.change_notification", login_url="login")
def update_notification(request, pk):
    notification = Notification.objects.get(id=pk)
    form = NotificationForm(instance=notification, use_required_attribute=False)
    if request.method == "POST":
        form = NotificationForm(request.POST, instance=notification, use_required_attribute=False)
        if form.is_valid():
            notification = form.save()
            return redirect("view-notification", notification.id)
    context = {"notification": notification, "form": form}
    return render(request, "notifications/update-notification.html", context)


@login_required(login_url="login")
@permission_required("notifications.delete_notification", login_url="login")
def delete_notification(request, pk):
    notification = Notification.objects.get(id=pk)
    notification.deleted = timezone.now()
    notification.save()
    return redirect("view-notifications")


@login_required(login_url="login")
@permission_required("notifications.add_notification", login_url="login")
def create_notification(request):
    form = NotificationForm(use_required_attribute=False)
    context = {"form": form}
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save()
            return redirect("view-notifications")
    return render(request, "notifications/create-notification.html", context)