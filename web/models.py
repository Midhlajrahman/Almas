from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    image = models.ImageField(upload_to="products/")
    size = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def get_absolute_url(self):
        return reverse("web:product_details", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class ProductEnquiry(models.Model):
    product = models.ForeignKey("web.Product", on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=120)
    message = models.CharField(max_length=900)

    class Meta:
        verbose_name = "Product Enquiry"
        verbose_name_plural = "Product Enquiries"

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    position = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to="testimonial-images",
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    image = models.ImageField(
        upload_to="blog-images/",
    )
    content = HTMLField()
    date = models.DateField()

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return str(self.title)


class Contact(models.Model):
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(db_index=True, auto_now_add=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=120, blank=True, null=True)
    subject = models.CharField(max_length=120, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)


class Enquiry(models.Model):
    service = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
