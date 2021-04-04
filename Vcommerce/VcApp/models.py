from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

# from djongo import models

# Create your models here.


class User(models.Model):
    CUSTOMER = 'cr'
    SELLER = 'sr'
    TYPE_CHOICES=(
        (CUSTOMER, 'Customer'),
        (SELLER, 'Seller')'
    )
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    phone = models.IntegerField()
    user_type = models.CharField(choices=TYPE_CHOICES, max_length=2)

class Product(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='VcApp/images')
    # option = models.ForeignKey(Product_option, on_delete=models.PROTECT)
    option = ListField(EmbeddedModelField(Product_option))
    create_date = models.DateField(auto_now_add=True)
    stock = models.IntegerField()
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # seller = models.ForeignKey(Seller, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='VcApp/Image')

class Product_category(models.Model):
    class Meta:
        verbose_name_plural = 'Product-categories'

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

# class Option(models.Model):
#     option_name = models.CharField(max_length=100)

# class Product_option(models.Model): 
#     option_type = models.CharField(max_length=100)
#     option_id = models.ForeignKey(Option, on_delete=models.CASCADE)
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Product_option(models.Model):
    option_type = models.CharField(max_length=100)
    option = ListField(EmbeddedModelField(Option))

class Option(models.Model):
    option_name = models.CharField(max_length=100)
    option_price = models.IntegerField()

# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254)
#     address = models.TextField()
#     phone = models.IntegerField()

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    amount = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    order_status = models.CharField(max_length=100)

class Order_detail(models.Model):
    ordier_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.IntegerField()
    quantity = models.IntegerField()

