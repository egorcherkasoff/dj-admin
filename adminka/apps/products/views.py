from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
from django.core.paginator import Paginator
from .filters import ProductFilter
from . import models
from ..tags.models import Tag


# Create your views here.
@login_required(login_url="login")
@permission_required("products.view_product")
def view_all_products(request):
    filter_products = ProductFilter(
        request.GET, queryset=models.Product.objects.filter(deleted__isnull=True)
    )
    paginator = Paginator(filter_products.qs, 20)
    if request.GET.get("page"):
        page_num = request.GET.get("page")
    else:
        page_num = 1
    products = paginator.page(page_num)
    context = {"filter_products": filter_products, "products": products}
    return render(request, "products/products.html", context)


@login_required(login_url="login")
@permission_required("products.view_product")
def view_products(request, pk):
    product = models.Product.objects.get(id=pk)
    images = product.images.all()
    tags = product.tags.all()
    context = {"product": product,"images":images , "tags": tags}
    return render(request, "products/view-product.html", context)


@login_required(login_url="login")
@permission_required("products.add_product")
def create_product(request):
    pass


@login_required(login_url="login")
@permission_required("products.change_product")
def update_product(request, pk):
    pass


@login_required(login_url="login")
@permission_required("products.delete_product")
def delete_product(request, pk):
    pass
