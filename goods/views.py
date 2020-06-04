from django.views.generic.base import TemplateView, View
from django.http import JsonResponse
from goods.models import Product


class GoodsCatalogView(TemplateView):

    template_name = 'goods/catalog.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['all_goods'] = Product.objects.all()
        return context


class AjaxCartRequest(View):

    def get(self):
        response = dict()
        if self.request.method == 'GET' and self.request.is_ajax():
            response['test'] = 'test_message'
        else:
            response['test'] = 'failed'
        return JsonResponse(response)
