from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductsList,ProductDetail
urlpatterns = [
    path('products/', ProductsList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)