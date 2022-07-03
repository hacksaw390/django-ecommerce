from django.contrib import admin
from .models import *
# Register your models here.


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


class ProductSpecificationInline(admin.StackedInline):
    model = Specification
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductSpecificationInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Tag)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Category)
