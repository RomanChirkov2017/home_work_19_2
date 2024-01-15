from django.shortcuts import render


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
