from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Product
from .models import Category


def home(request):

    products = Product.objects.filter(
        available=True
    )[:8]

    return render(
        request,
        'store/home.html',
        {
            'products': products
        }
    )


def product_list(request):

    category_slug = request.GET.get(
        'category'
    )

    products = Product.objects.filter(
        available=True
    )

    categories = Category.objects.all()

    if category_slug:
        products = products.filter(
            category__slug=category_slug
        )

    return render(
        request,
        'store/product_list.html',
        {
            'products': products,
            'categories': categories
        }
    )


def product_detail(
    request,
    slug
):

    product = get_object_or_404(
        Product,
        slug=slug,
        available=True
    )

    return render(
        request,
        'store/product_detail.html',
        {
            'product': product
        }
    )


def search_products(request):

    query = request.GET.get(
        'q'
    )

    products = Product.objects.filter(
        name__icontains=query
    ) if query else []

    return render(
        request,
        'store/search.html',
        {
            'products': products,
            'query': query
        }
    )
