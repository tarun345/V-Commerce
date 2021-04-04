from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register, name='register'),
    path('categories/<str:pk>/', views.categories, name='categories'),
    path('categories/', views.categories, name='categories'),
    path('product/<str:pk>/', views.getproduct, name='product'),
    path('addProd/', views.addProd, name='addProd'),
    path('deals/', views.deals, name='deals'),
    path('sell/', views.sell, name='sell'),
    path('acount/<str:pk>/', views.acount, name='acount'),
    path('acount', views.acount, name='acount'),
    path('voice_command', views.voice_command, name="voice_command"),
    path('search_products', views.search_products, name="search_products"),
    path('cart/<str:pk>/', views.cart, name='cart'),
    path('cart', views.cart, name='cart'),
    path('removeItem/<str:pk>/', views.removeItem, name='removeItem'),
    path('updateItem/<str:pk>/', views.updateItem, name='updateItem'),
    path('checkout', views.checkout, name='checkout'),
    path('mkorders', views.mkorders, name='mkorders'),
    path('mkorders/<int:pk>/', views.mkorders, name='mkorders'),
    path('updateItem', views.updateItem, name='updateItem'),
]