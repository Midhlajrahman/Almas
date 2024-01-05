from django.contrib import admin

from .models import Blog, Contact, Enquiry, Product, ProductEnquiry, Testimonial


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "size",
    )
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProductEnquiry)
class ProductEnquiryAdmin(admin.ModelAdmin):
    list_display = ("product", "name", "email", "phone")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "position",
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
    )


@admin.register(Enquiry)
class EnquiryForm(admin.ModelAdmin):
    list_display = ("name", "email", "message")
