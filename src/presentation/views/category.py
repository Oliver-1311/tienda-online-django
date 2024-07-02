from django.views import View
from django.http import JsonResponse

class CategoryView(View):

    def get(self, request):
        return JsonResponse({ 'mensaje': 'Category'})