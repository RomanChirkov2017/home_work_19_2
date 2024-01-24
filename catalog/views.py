from django.shortcuts import render

from catalog.models import Category, Product


def index(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        query = request.POST.get('query')
        print(f"{value}, {query}")
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        print(f"{name}, {email}, {phone}")
    return render(request, 'catalog/contacts.html')


def category_products(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Все категории'
    }
    return render(request, 'catalog/categories.html', context)


def products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'{category_item.name}'
    }
    return render(request, 'catalog/products.html', context)

