from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
from django.core.paginator import Paginator
from .filters import ShipmentFilter
from .models import Shipment
from .forms import ShipmentForm, ViewShipment
from django.http import HttpResponseRedirect


# Create your views here.
@login_required(login_url="login")
@permission_required("shipments.view_shipment")
def view_all_shipments(request):
    filter = ShipmentFilter(
        request.GET, queryset=Shipment.objects.filter(deleted__isnull=True)
    )
    paginator = Paginator(filter.qs, 20)
    if request.GET.get("page"):
        page_num = request.GET.get("page")
    else:
        page_num = 1
    shipments = paginator.page(page_num)
    context = {"filter": filter, "shipments": shipments}
    return render(request, "shipments/shipments.html", context)


@login_required(login_url="login")
@permission_required("shipments.view_shipment")
def view_shipment(request, pk):
    shipment = Shipment.objects.get(id=pk)
    form = ViewShipment(instance=shipment)
    images = shipment.images.all()
    tags = shipment.tags.all()
    context = {"shipment": shipment, "images": images, "tags": tags, "form": form}
    return render(request, "shipments/view-shipment.html", context)


@login_required(login_url="login")
@permission_required("shipments.add_shipment")
def create_shipment(request):
    form = ShipmentForm()
    context = {"form": form}
    if request.method == "POST":
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save()
            return redirect("view-shipments")
    return render(request, "shipments/create-shipment.html", context)


@login_required(login_url="login")
@permission_required("shipments.change_shipment")
def update_shipment(request, pk):
    shipment = Shipment.objects.get(id=pk)
    products = shipment.shipment_products.all()
    form = ShipmentForm(instance=shipment)
    if request.method == "POST":
        form = ShipmentForm(request.POST, instance=shipment)
        shipment = form.save()
        return redirect("view-shipment", shipment.id)
    context = {
        "shipment": shipment,
        "products": products,
        "form": form,
    }
    return render(request, "shipments/update-shipment.html", context)


@login_required(login_url="login")
@permission_required("shipments.delete_shipment")
def delete_shipment(request, pk):
    shipment = Shipment.objects.get(id=pk)
    shipment.deleted = timezone.now()
    shipment.save()
    return redirect("view-shipments")


# @login_required(login_url="login")
# @permission_required("shipments.change_shipment")
# def update_shipment_tags(request, pk):
#     shipment = Shipment.objects.get(id=pk)
#     shipment_tags = shipment.tags.filter(deleted__isnull=True)
#     tags = Tag.objects.exclude(shipment__id=shipment.id)
#     context = {"shipment": shipment, "shipment_tags": shipment_tags, "tags": tags}
#     return render(request, "shipments/update-shipment-tags.html", context)


# @login_required(login_url="login")
# @permission_required("shipments.change_shipment")
# def add_shipment_tag(request, pk, tag_id):
#     shipment = Shipment.objects.get(id=pk)
#     shipment.tags.add(tag_id)
#     return redirect("update-shipment-tags", pk)


# @login_required(login_url="login")
# @permission_required("shipments.change_shipment")
# def remove_shipment_tag(request, pk, tag_id):
#     shipment = Shipment.objects.get(id=pk)
#     shipment.tags.remove(tag_id)
#     return redirect("update-shipment-tags", pk)
