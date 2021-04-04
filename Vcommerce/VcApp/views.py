from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'VcApp/index.html')
def login(request):
    return render(request, 'VcApp/login.html')
def register(request):
    return render(request, 'VcApp/register.html')
def acount(request):
    return render(request, 'VcApp/acount.html')
def categories(request):
    return render(request, 'VcApp/categories.html')
