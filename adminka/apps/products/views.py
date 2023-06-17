from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
from django.core.paginator import Paginator
from .filters import ProductFilter
from . import models
from ..tags.models import Tag
from .forms import ProductUpdateForm, ProductImagesForm
from django.http import HttpResponseRedirect
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
    product = models.Product.objects.get(id=pk)
    images = product.images.all()
    tags = product.tags.all()
    form = ProductUpdateForm(instance=product)
    image_form = ProductImagesForm()
    if request.method == "POST":
        if "name" in request.POST:
            form = ProductUpdateForm(request.POST, instance=product)
            product = form.save()
            product.updated = timezone.now()
            product.save()
            return redirect("view-product", product.id)
        if request.FILES:
            for file in request.FILES.getlist('image'):  # Получаем список всех файлов
                product_image = models.ProductImage(product=product, image=file)
                product_image.save()
            return redirect("view-product", product.id)
    context = {"product": product, "images": images, "tags":tags, "form": form, "image_form":image_form}
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
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))