from django.shortcuts import render, redirect
from .assistant import takeCommand, speak, search
from .models import *
from math import ceil

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, AddProductForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only

from django.contrib.auth.models import Group

from django.http import JsonResponse

# Create your views here.
def index(request):
    
    # g = request.user.groups.all()
    # print(g[0:], g[1])
    # print(g)
    # for i in g:
    #     print(i.name)

    allprods = []
    brands = Product.objects.values('company')
    brs = {item['company'] for item in brands}
    for br in brs:
        prod = Product.objects.filter(company=br)
        n = len(prod)
        nSlides = n//3 + ceil((n/3)-(n//3))
        print(n)
        print(nSlides)
        allprods.append([prod, range(nSlides), nSlides])

    params = {'allprod':allprods }
    return render(request, 'homePage/index.html', params)

@unauthenticated_user
def loginUser(request):
 
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username or password is incorrect')
    return render(request, 'homePage/login.html')
   

def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def register(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Customer')
            user.groups.add(group)

            UserProfile.objects.create(
                user = user,
                name = username,
            )
            

            messages.success(request, 'Acount was created for '+username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'homePage/register.html', context)

   
    
@login_required(login_url='login')
def acount(request, pk=''):
    return render(request, 'homePage/acount.html')

@login_required(login_url='login')
def cart(request, pk=''):
    user_profile = UserProfile.objects.get(user=request.user)
    user_order, status = Order.objects.get_or_create(customer = user_profile)

    if pk != '':
        product = Product.objects.get(id=pk)
        order_item, status = OrderItem.objects.get_or_create(product = product)
        user_order.items.add(order_item)
        user_order.ref_code = user_order.id*12//3*44
        user_order.save()
        
    print(user_order.items)
    print(user_order.get_cart_items())
    content = {'orders':user_order}
    return render(request, 'homePage/cart.html', content)

def removeItem(request, pk=''):
    order_item = OrderItem.objects.get(id=pk)
    user_profile = UserProfile.objects.get(user=request.user)
    user_order= Order.objects.get(customer = user_profile)
    user_order.items.remove(order_item)
    return redirect('cart')

def updateItem(request, pk):
    order_item = OrderItem.objects.get(id=pk)
    order_item.quantity = request.GET.get('quantity')
    order_item.save()
    return redirect('cart')



@login_required(login_url='login')
# @allowed_users(allowed_roles=['Customer'])

def mkorders(request, pk=''):
    print("pk valu", pk)
    user_profile = UserProfile.objects.get(user=request.user)
    user_order, status = Order.objects.get_or_create(customer = user_profile)

    if pk != '':
        product = Product.objects.get(id=pk)
        order_item, status = OrderItem.objects.get_or_create(product = product)
        user_order.items.add(order_item)
        user_order.ref_code = user_order.id*12//3*44
        user_order.save()

    orders = request.user.userprofile.order_set.all()
    print("ORDERS for:",request.user.username, orders)
    context = {'orders': orders}
    return render(request, 'homePage/orders.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Seller', 'admin', 'Customer'])
def checkout(request):
    m = request.GET.get('pmode')
    user_profile = UserProfile.objects.get(user = request.user)
    order_user = Order.objects.get(customer = user_profile)
    order_user.payment_code = m
    print(order_user.items)
    print(order_user.get_cart_items())
    itms = order_user.get_cart_items()
    for i in itms:
        i.product.ordered = True
        i.product.save()
        print(i.product.ordered)
    content = {"order":order_user}
    order_user.save()
    # itms = order_user.items
    # print(itms)
    return render(request, 'homePage/checkout.html', content)
    
def categories(request, pk=''):
    if pk == '':
        content = Categories.objects.all()
        return render(request, 'homePage/categories.html', {'cat': content})

    else:
        cat = Categories.objects.get(id=pk)
        content = Product.objects.filter(category=cat)
        return render(request, 'homePage/cateProducts.html', {'prod': content})

def voice_command(request):
    query = takeCommand()
    results = search(query)
    return render(request, 'homePage/results.html', {'res':results, 'query':query})

def search_products(request):
    query = request.GET.get('search', '')
    results = search(query)
    print(results)
    return render(request, 'homePage/results.html', {'res':results, 'query':query})
    
def getproduct(request, pk=''):
    if pk != '':
        content = Product.objects.get(id=pk)
        return render(request, 'homePage/product.html', {'prod': content})
        
def addProd(request):
    form = AddProductForm()
    context = {'form': form}
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
                product = form.save()
                pname = form.cleaned_data.get('name')
                seller = UserProfile.objects.get(user=request.user)
                product.seller.add(seller)
                messages.success(request, pname, 'Produt was added for ')
                return redirect('addProd')

    return render(request, 'homePage/addProduct.html', context)

def deals(request):
    seller = UserProfile.objects.get(user=request.user)
    prod = Product.objects.filter(seller = seller)
    print(prod)
    oredered_prod = [p for p in prod if p.ordered == True]
    print("ordered:", oredered_prod)
    oredered_items = [OrderItem.objects.filter(product = i) for i in oredered_prod]
    print(oredered_items)
    ord = Order.objects.all()
    print(ord)
    # i = OrderItem.objects.get(id=7)
    # cust_order = i.order_set.all()
    cust_order = [j.order_set.all() for i in oredered_items for j in i]
    print(cust_order)
    context = {'products': oredered_prod}
    return render(request, 'homePage/deals.html', context)


@login_required(login_url='login')
def sell(request):
    user = request.user
    group = Group.objects.get(name='Seller')
    user.groups.add(group)
    return redirect('index')

