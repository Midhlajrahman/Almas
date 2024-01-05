from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("products/", views.products, name="products"),
    path("product/", views.product_details, name="product_details"),
    path("product/<slug:slug>/", views.product_details, name="product_details"),
    path("blog/", views.blog, name="blog"),
    path("blog-details/<slug:slug>", views.blog_details, name="blog-details"),
    path("contact/", views.contact, name="contact"),
]
