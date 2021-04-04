from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateSellerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name', 'company', 'price', 'description', 'thumbnail', 'stock', 'category']
