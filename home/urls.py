from django.urls import path
from .views import HomeIndexView

urlpatterns = [
    path('', HomeIndexView.as_view(), name='main')
]
