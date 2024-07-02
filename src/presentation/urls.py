from django.urls import path
from src.presentation.views import ProductView
from src.presentation.views import CategoryView

urlpatterns = [
    path('product/detail/', ProductView.as_view(), name='product-detail'),

    path('category/detail/', CategoryView.as_view(), name='category-detail'),
]