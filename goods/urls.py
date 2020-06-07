from django.urls import path
from .views import GoodsCatalogView

urlpatterns = [
    path('catalog', GoodsCatalogView.as_view(), name='catalog'),
]
