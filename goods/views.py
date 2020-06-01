from django.views.generic.base import TemplateView
from goods.models import Product


class GoodsCatalogView(TemplateView):

    template_name = 'goods/catalog.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['all_goods'] = Product.objects.all()
        return context
