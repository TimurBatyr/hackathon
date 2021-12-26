from django.shortcuts import get_object_or_404, render

from .models import Category, Product

def product_all(request):
    products = Product.products.all()
    return render(request, 'main/index.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'main/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'main/meal.html', {'product': product})