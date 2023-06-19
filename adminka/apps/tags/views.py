from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Tag
from .filters import TagFilter
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import TagForm, ViewTag
from django.utils import timezone

# Create your views here.
@login_required(login_url="login")
@permission_required("tags.view_tag", login_url="login")
def view_all_tags(request):
    filter = TagFilter(
        request.GET, queryset=Tag.objects.filter(deleted__isnull=True).order_by("name")
    )
    paginator = Paginator(filter.qs, 20)
    if request.GET.get("page"):
        page_num = request.GET.get("page")
    else:
        page_num = 1
    tags = paginator.page(page_num)
    context = {"tags": tags, "filter": filter}
    return render(request, "tags/tags.html", context)


@login_required(login_url="login")
@permission_required("tags.view_tag", login_url="login")
def view_tag(request, pk):
    tag = Tag.objects.get(id=pk)
    form = ViewTag(instance=tag)
    context = {"tag": tag, "form":form}
    return render(request, "tags/view-tag.html", context)


@login_required(login_url="login")
@permission_required("tags.change_tag", login_url="login")
def update_tag(request, pk):
    tag = Tag.objects.get(id=pk)
    form = TagForm(instance=tag)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            tag = form.save()
            return redirect("view-tag", tag.id)
    context = {"tag": tag, "form": form}
    return render(request, "tags/update-tag.html", context)


@login_required(login_url="login")
@permission_required("tags.delete_tag", login_url="login")
def delete_tag(request, pk):
    tag = Tag.objects.get(id=pk)
    tag.deleted = timezone.now()
    tag.save()
    return redirect("view-tags")


@login_required(login_url="login")
@permission_required("tags.add_tag", login_url="login")
def create_tag(request):
    form = TagForm()
    context = {"form": form}
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("view-tags")
    return render(request, "tags/create-tag.html", context)