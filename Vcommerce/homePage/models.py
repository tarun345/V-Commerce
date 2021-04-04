from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# from djongo import models

# Create your models here.

# class User(AbstractUser):
#     is_customer = models.BooleanField(default=False)
#     is_seller = models.BooleanField(default=False)


class UserProfile(models.Model):
    # CUSTOMER = 'cr'
    # SELLER = 'sr'
    # BOTH = 'bo'
    # TYPE_CHOICES = (
    #     (CUSTOMER, 'Customer'),
    #     (SELLER, 'Seller'),
    #     (BOTH, 'Both')
    # )
    # user_type = models.CharField(choices=TYPE_CHOICES, max_length=2, null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    # password = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)
    address = models.TextField(null=True)
    phone = models.IntegerField(null=True)
    def __str__(self):
        return self.name

    def seller_products(self):
        self.p = Product.object.filter(seller = self)
        return self.p
   

class Categories(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to='homePage/Image/categories', null=True)
    # product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

class Companies(models.Model):
    class Meta:
        verbose_name_plural = 'Companies'
    
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to='homePage/Image/companies', null=True)
    # product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    company = models.ForeignKey(Companies, on_delete= models.SET_NULL, null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
    # details = models.TextField(default='')
    thumbnail = models.ImageField(upload_to='homePage/images/products', default='', null=True)
    # updoad = models.FileField(upload_to='homePage/updoads', default='', null=True)
    # option = models.ManyToManyField(Product_option)
    create_date = models.DateField(auto_now_add=True)
    stock = models.IntegerField(null=True)
    category = models.ManyToManyField(Categories)
    seller = models.ManyToManyField(UserProfile)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    
# class Product_Categories(models.Model):
#     class Meta:
#         verbose_name_plural = 'Product-categories'

#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     Categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return self.name

class Option(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    option_name = models.CharField(max_length=100, null=True)
    option_thumbnail = models.ImageField(upload_to='homePage/images/products/options', default='', null=True)
    option_description = models.TextField(default='', null=True)

# class Product_option(models.Model): 
#     option_type = models.CharField(max_length=100)
#     option = models.ForeignKey(Option, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)

class OrderItem(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.OneToOneField(Product, on_delete=models.SET_NULL , null=True)
    quantity = models.IntegerField(default=1)
    order_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.product.name  
    def items_price(self):
        return (self.product.price * self.quantity)

class Order(models.Model):
    ref_code = models.CharField(max_length=15, null=True)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(OrderItem)
    # Product = models.ForeignKey(Product, on_delete=models.SET_NULL , null=True)
    # amount = models.IntegerField(null=True)
    # transaction_id = models.CharField
    order_date = models.DateField(auto_now_add=True)
    
    PENDING = 'pd'
    DONE = 'dn'
    PAYMENT_STATUS = (
        (PENDING, 'Pendin'),
        (DONE, 'Done')
    )
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=2, null=True)

    COD = 'co'
    CARD = 'ca'
    NET_BANKING = 'nb'
    PAYMENT_MODE = (
        (COD, 'COD'),
        (CARD, 'Card'),
        (NET_BANKING, 'Net Banking')
    )
    payment_mode = models.CharField(choices=PAYMENT_MODE, max_length=2, null=True)

    OUt_FOR_DELIVERY = 'od'
    DELIVERED = 'de'
    DELIVERY_STATUS = (
        (PENDING, 'Pendin'),
        (OUt_FOR_DELIVERY, 'Out For Delivery'),
        (DELIVERED, 'Delivered')
    )
    delivery_status = models.CharField(choices=DELIVERY_STATUS, max_length=2, null=True)

    # def get_cart_total(self):
    #     return sum([item.product.price for item in self.items.all()])

    def get_cart_total(self):
        return sum([item.items_price() for item in self.items.all()])

    def get_cart_items(self):
        return self.items.all()     

    def get_sellers(self):
        return [item.product.seller for item in self.items.all()]
    
    def __str__(self):
        return '{0}-{1}'.format(self.customer, self.ref_code)



    # order_status = models.CharField(max_length=100, null=True)

# class Order_detail(models.Model):
#     ordier_id = models.ForeignKey(Order, on_delete=models.PROTECT , null=True)
#     product_id = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
#     price = models.IntegerField(null=True)
#     quantity = models.IntegerField(null=True)

