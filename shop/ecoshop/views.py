import datetime

from django.shortcuts import render
from django.http import HttpResponse

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

GOODS = {
    "apple": {
        "cost":4.24,
        "count": 1000,
        "delive":["Belarus","Poland","Russia"]
    },
    "orange": {
        "cost": 7.24,
        "count": 100,
        "delive":["SAR","Spain","Portugal"]
    },
    "grape": {
        "cost": 11.33,
        "count": 1000,
        "delive": ["Spain","Turkey","Italy"]
    }
}


def index_ecoshop(request):
    return render(request,"index.html")


def info_ecoshop(request,ecoshop,street,number):
    context = {
        "ecoshop": ecoshop,
        "street":street,
        "number":number
    }
    return render(request,"info.html",context=context)


def regular_year_views(request,year):
    return HttpResponse(f"year build is {year}")


def data_user_views(request):
    user = User("Vasya",23)
    context = {
        "user": user,
    }
    return render(request, "get_data_user.html", context=context)

def goods_catalog(request):
    context = {
        "goods": GOODS
    }
    return render(request, "goods_catalog.html", context=context)