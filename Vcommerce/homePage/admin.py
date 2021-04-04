from django.contrib import admin
from .models import *

# register your models here.
admin.site.register(Product)
# admin.site.register(Product_option)
admin.site.register(Option)
admin.site.register(Companies)
admin.site.register(Categories)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)