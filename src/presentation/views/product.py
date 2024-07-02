from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from src.application.use_cases import ProductUseCase
from src.infrastructure.repositories import ProductRepository

class ProductView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.productRepository = ProductRepository()
        self.productUseCase = ProductUseCase(self.productRepository)

    def get(self, request):
        data = self.productUseCase.detail()
        return JsonResponse({ 'mensaje': data})