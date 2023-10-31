import pdb

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView

from .forms import ProductsReviewsForm
from .models import ProductsReviews, Person, Product, Reviews


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


GOODS = {
    "apple": {
        "price": 4.24,
        "id": 1
    },
    "orange": {
        "price": 4.24,
        "id": 2
    },
    "grape": {
        "price": 4.24,
        "id": 3
    }
}


class MyView(TemplateView):
    template_name = "info.html"


def index_ecoshop(request):
    return render(request, "index.html")


def comments(request):
    comments = ProductsReviews.objects.select_related("product").prefetch_related("product__person_set").all()
    persons = Person.objects.prefetch_related("product").all()
    context = {
        "comments": comments,
        "persons": persons
    }

    return render(request, "comments.html", context=context)


# def products(request):
#     products = Product.objects.filter(price__gt=0.5).order_by("amount")[:100]
#     context = {
#         "products": products
#     }
#     return render(request, "products.html", context=context)


class ProductViews(ListView):
    template_name = "products.html"
    model = Product
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["products"] = Product.objects.all()
    #     return context

class ReviewFormView(FormView):
    template_name = "create_review_product.html"
    form_class = ProductsReviewsForm
    success_url = "/ecoshop/comments/"


# def create_review(request):
#     context = {}
#
#     if request.method == "POST":
#         form = ProductsReviewsForm(request.POST)
#         form.save()
#         if form.is_valid():
#             # reviews = ProductsReviewsForm(
#             #     **form.cleaned_data
#             # )
#             # reviews.save()
#             return HttpResponseRedirect("/ecoshop/comments/")
#     else:
#         form = ProductsReviewsForm()
#
#     context["form"] = form
#     return render(request, "create_review_product.html", context=context)
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
