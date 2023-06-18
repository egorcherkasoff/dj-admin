from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
from django.core.paginator import Paginator
from .filters import ProductFilter
from . import models
from ..tags.models import Tag
from .forms import ProductForm, ProductImagesForm, ViewProduct
from django.http import HttpResponseRedirect


# Create your views here.
@login_required(login_url="login")
@permission_required("products.view_product")
def view_all_products(request):
    filter = ProductFilter(
        request.GET, queryset=models.Product.objects.filter(deleted__isnull=True)
    )
    paginator = Paginator(filter.qs, 20)
    if request.GET.get("page"):
        page_num = request.GET.get("page")
    else:
        page_num = 1
    products = paginator.page(page_num)
    context = {"filter": filter, "products": products}
    return render(request, "products/products.html", context)


@login_required(login_url="login")
@permission_required("products.view_product")
def view_products(request, pk):
    product = models.Product.objects.get(id=pk)
    form = ViewProduct(instance=product)
    images = product.images.all()
    tags = product.tags.all()
    context = {"product": product, "images": images, "tags": tags, "form": form}
    return render(request, "products/view-product.html", context)


@login_required(login_url="login")
@permission_required("products.add_product")
def create_product(request):
    form = ProductForm()
    context = {"form": form}
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect("view-products")
    return render(request, "products/create-product.html", context)


@login_required(login_url="login")
@permission_required("products.change_product")
def update_product(request, pk):
    product = models.Product.objects.get(id=pk)
    images = product.images.all()
    tags = product.tags.all()
    form = ProductForm(instance=product)
    image_form = ProductImagesForm()
    if request.method == "POST":
        if "name" in request.POST:
            form = ProductForm(request.POST, instance=product)
            product = form.save()
            product.updated = timezone.now()
            product.save()
            return redirect("view-product", product.id)
        if request.FILES:
            for file in request.FILES.getlist("image"):
                product_image = models.ProductImage(product=product, image=file)
                product_image.save()
            return redirect("view-product", product.id)
    context = {
        "product": product,
        "images": images,
        "tags": tags,
        "form": form,
        "image_form": image_form,
    }
    return render(request, "products/update-product.html", context)


@login_required(login_url="login")
@permission_required("products.delete_product")
def delete_product(request, pk):
    product = models.Product.objects.get(id=pk)
    product.deleted = timezone.now()
    product.save()
    return redirect("view-products")


@login_required(login_url="login")
@permission_required("products.change_product")
def delete_product_image(request, pk, img_id):
    image = models.ProductImage.objects.get(id=img_id)
    image.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required(login_url="login")
@permission_required("products.change_product")
def update_product_tags(request, pk):
    product = models.Product.objects.get(id=pk)
    product_tags = product.tags.filter(deleted__isnull=True)
    tags = Tag.objects.exclude(product__id=product.id)
    context = {"product": product, "product_tags": product_tags, "tags": tags}
    return render(request, "products/update-product-tags.html", context)


@login_required(login_url="login")
@permission_required("products.change_product")
def add_product_tag(request, pk, tag_id):
    product = models.Product.objects.get(id=pk)
    product.tags.add(tag_id)
    return redirect("update-product-tags", pk)


@login_required(login_url="login")
@permission_required("products.change_product")
def remove_product_tag(request, pk, tag_id):
    product = models.Product.objects.get(id=pk)
    product.tags.remove(tag_id)
    return redirect("update-product-tags", pk)
    
