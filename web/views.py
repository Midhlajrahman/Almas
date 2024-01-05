
from django.http import JsonResponse
from django.shortcuts import render

from web.forms import ContactForm, EnquiryForm, ProductEnquiryForm

from .models import Blog, Product, Testimonial


def index(request):
    products = Product.objects.all()
    blog = Blog.objects.all()
    testimonial = Testimonial.objects.all()

    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            form.save()
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
        form = EnquiryForm()  # Move this line outside the else block
        context = {
            "is_index": True,
            "products": products,
            "testimonial": testimonial,
            "blog": blog,
            "form": form,
        }
        return render(request, "web/index.html", context)


def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)


def products(request):
    products = Product.objects.all()
    context = {"is_products": True, "products": products}
    return render(request, "web/products.html", context)


def product_details(request, slug):
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
    blog = Blog.objects.all()

    context = {"is_blog": True, "blog": blog}
    return render(request, "web/blog.html", context)


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        "blog": blog,
    }

    return render(request, "web/blog-details.html", context)


def contact(request):
    form = ContactForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
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
            # "is_contact": True,
            "form": ContactForm(),
        }
    return render(request, "web/contact.html", context)
