from django.views.generic.base import View
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Sum
from goods.models import Product, Cart


class GoodsCatalogView(View):

    template_name = 'goods/catalog.html'

    def get(self, *args):
        if not self.request.is_ajax():
            context = dict()
            context['all_goods'] = Product.objects.all()
            return render(self.request, self.template_name, context)
        else:
            pid = self.request.GET.get('pid')
            price = self.request.GET.get('price')
            uid = self.request.user.id
            # Cart.objects.create(product_id=pid, user_id=1, amount=1)

            user_goods = Cart.objects.filter(user_id=uid)
            goods_count = user_goods.count()
            goods_amount = 100

            response = dict()
            response['test'] = f'Сохранены данные: {pid} / {price}'
            response['count'] = goods_count
            response['amount'] = goods_amount
            return JsonResponse(response)
