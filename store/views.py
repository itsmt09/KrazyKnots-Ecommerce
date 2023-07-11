from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from carts.models import CartItem
from carts.views import _cart_id

from store.models import Product
from category.models import Category
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def store(request, category_slug = None):

    categories = None
    products = None
    page_obj = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category = categories, is_available = True).order_by("id")
        paginator = Paginator(products, 1)
        page_number = request.GET.get("page") # 'page' is a query string in link ?page=3
        page_obj = paginator.get_page(page_number)

    else:
        products = Product.objects.all().filter(is_available = True).order_by("id")
        paginator = Paginator(products, 2)
        page_number = request.GET.get("page") # 'page' is a query string in link ?page=3
        page_obj = paginator.get_page(page_number)

    product_count = products.count()

    context = {
        'products': page_obj,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product = single_product).exists()
    except Exception as e:
        raise e

    context = {
        'single_product' : single_product,
        'in_cart' : in_cart,
    }
    return render(request, 'store/product_detail.html', context)

def search(request):
    page_obj = None
    product_count = 0
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword)
                        | Q(product_name__icontains=keyword) | Q(brand_name__icontains=keyword))
            product_count = products.count()
            # pagination
            paginator = Paginator(products, 1)
            page_number = request.GET.get("page") # 'page' is a query string in link ?page=3
            page_obj = paginator.get_page(page_number)

    context = {
        'products' : page_obj,
        'product_count' : product_count,
    }
    return render(request, 'store/store.html', context)
