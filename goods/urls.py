from django.urls import path
from .views import GoodsCatalogView, AjaxCartRequest


urlpatterns = [
    path('catalog', GoodsCatalogView.as_view(), name='catalog'),
    path('', AjaxCartRequest.as_view(), name='ajax_cart')
]
