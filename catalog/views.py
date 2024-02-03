from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Category, Product, Blog


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Главная'
    }

#def index(request):
#    if request.method == 'POST':
#        value = request.POST.get('value')
#        query = request.POST.get('query')
#        print(f"{value}, {query}")
#    return render(request, 'catalog/index.html')


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

#def contacts(request):
#    if request.method == 'POST':
#        name = request.POST.get('name')
#        email = request.POST.get('email')
#        phone = request.POST.get('phone')
#        print(f"{name}, {email}, {phone}")
#    return render(request, 'catalog/contacts.html')


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Все категории'
    }

#def category_products(request):
#    context = {
#        'object_list': Category.objects.all(),
#        'title': 'Все категории'
#    }
#    return render(request, 'catalog/category_list.html', context)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk
        context_data['title'] = f'{category_item.name}'
        return context_data

#def products(request, pk):
#    category_item = Category.objects.get(pk=pk)
#    context = {
#        'object_list': Product.objects.filter(category_id=pk),
#        'title': f'{category_item.name}'
#    }
#    return render(request, 'catalog/product_list.html', context)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'{category_item.name}'

        return context_data

#def product_item(request, pk):
#    context = {
#        'object': Product.objects.get(pk=pk),
#    }
#    return render(request, 'catalog/product_detail.html', context)


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Блог'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.view_count += 1
        self.object.save()
        return self.object

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Blog.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'{category_item.name}'
        return context_data


class BlogCreateView(CreateView):
    model = Blog
    extra_context = {
        'title': 'Создание статьи'
    }
    fields = ('name', 'content', 'image')
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'content', 'image',)
    # success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_item', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')

