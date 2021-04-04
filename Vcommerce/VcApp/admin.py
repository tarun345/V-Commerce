from django.contrib import admin
from .models import Product,Product_category, Category, Product_option, Option, User, Order, Order_detail

# register your models here.
admin.site.register(Product)
admin.site.register(Product_option)
admin.site.register(Option)
admin.site.register(Product_category)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Order_detail)