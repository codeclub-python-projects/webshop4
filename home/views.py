from django.views.generic.base import TemplateView
from django.db.models import Count
from goods.models import Product


class HomeIndexView(TemplateView):

    template_name = 'home/index.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['new_goods'] = Product.objects.all()[:10]
        context['top_goods'] = Product.objects.annotate(num_cart=Count('cart')).order_by('-num_cart')[:20]
        return context
