from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    sku = models.IntegerField()
    quantity = models.IntegerField()
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    color = models.ManyToManyField(Color, related_name='color_set')
    size = models.ManyToManyField(Size, related_name='size_set')
    short_description = models.TextField(max_length=200)
    feature = RichTextField()
    tag = models.ManyToManyField(Tag, related_name='tag_set')
    # image = models.ImageField()
    # image = models.ForeignKey(ProductImage, on_delete=models.CASCADE)

    @property
    def all_image(self):
        all_image = self.images.all()
        return all_image

    @property
    def all_specification(self):
        all_specification = self.specification.all()
        return all_specification

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product/product/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)


class Specification(models.Model):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name='specification', on_delete=models.CASCADE)


    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transection_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
