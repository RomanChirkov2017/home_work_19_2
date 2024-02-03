from django.urls import path

from catalog.apps import MainConfig
from catalog.views import IndexView, ContactView, ProductListView, CategoryListView, ProductDetailView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView, BlogListView, BlogDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category_products/', CategoryListView.as_view(), name='category_products'),
    path('<int:pk>/products/', ProductListView.as_view(), name='products'),
    path('contacts', ContactView.as_view(), name='contacts'),
    path('<int:pk>/product_item', ProductDetailView.as_view(), name='product_item'),
    path('blog', BlogListView.as_view(), name='blog'),
    path('catalog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('catalog/update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('catalog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('<int:pk>/blog_item', BlogDetailView.as_view(), name='blog_item'),
]


