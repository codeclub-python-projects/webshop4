from django.urls import path
from .views import GoodsCatalogView


urlpatterns = [
    path('category', GoodsCatalogView.as_view(), name='catalog')
]
