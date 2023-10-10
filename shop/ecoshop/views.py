from django.http import HttpResponse
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
    return render(request, "comments.html")

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
