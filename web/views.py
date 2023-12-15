from django.http import JsonResponse
from django.shortcuts import render

from web.forms import (
    ProductEnquiryForm
)

from .models import Product

def index(request):
    products = Product.objects.all()
    context = {"is_index": True,
               "products": products
               }
    return render(request, "web/index.html", context)


def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)


def products(request):
    products = Product.objects.all()
    context = {"is_products": True,
                "products": products
                }
    return render(request, "web/products.html", context)


def product_details(request,slug):
    product = Product.objects.get(slug=slug)
    other_products = Product.objects.exclude(slug=slug)
    form = ProductEnquiryForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)
            data.product = product
            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {"status": "false", "title": "Form validation error"}
        return JsonResponse(response_data)
    else:
        context = {
            "is_products": True,
            "product": product,
            "other_products": other_products,
            "form": ProductEnquiryForm(),
        }
    return render(request, "web/product-details.html", context)


def blog(request):
    context = {"is_blog": True}
    return render(request, "web/blog.html", context)


def contact(request):
    context = {"is_contact": True}
    return render(request, "web/contact.html", context)