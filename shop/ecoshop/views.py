from django.http import HttpResponse
from .models import ProductsReviews,Person
from django.shortcuts import render


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


GOODS = {
    "apple":{
        "price": 4.24,
        "id":1
    },
    "orange":{
        "price": 4.24,
        "id":2
    },
    "grape":{
        "price": 4.24,
        "id":3
    }
}


def index_ecoshop(request):
    return render(request, "index.html")

def comments(request):
    comments = ProductsReviews.objects.select_related("product").prefetch_related("product__person_set").all()
    persons = Person.objects.prefetch_related("product").all()
    context = {
        "comments": comments,
        "persons": persons
    }

    return render(request, "comments.html",context=context)

def products(request):
    context = {
        "goods": GOODS
    }
    return render(request, "products.html", context=context)
# def info_ecoshop(request, ecoshop, street, number):
#     context = {
#         "ecoshop": ecoshop,
#         "street": street,
#         "number": number
#     }
#     return render(request, "info.html", context=context)
#
#
# def regular_year_views(request, year):
#     return HttpResponse(f"year build is {year}")




#
# def goods_catalog(request):
#     context = {
#         "goods": GOODS
#     }
#     return render(request, "goods_catalog.html", context=context)
