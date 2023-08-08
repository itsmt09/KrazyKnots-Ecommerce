"""krazyknots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name = 'cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name = 'add_cart'),
    path('decrease_cart_item/<int:product_id>/<int:cart_item_id>/', views.decrease_cart_item, name = 'decrease_cart_item'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name = 'remove_cart_item'),
    # use product id here and also category id
]
