from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from .forms import ProductsReviewsForm, ProductForm
from .models import ProductsReviews, Person, Product
from .tasks import summa, generate_photo, send_msg_for_mail


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
    # summa.apply_async((2, 3))
    # send_msg_for_mail.apply_async(("djangotester28@gmail.com",))
    return render(request, "index.html")


# @cache_page(60,cache="redis_cache")
@permission_required("ecoshop.delete_product", raise_exception=True)
@login_required(login_url="/admin/accounts/login/")
def comments(request):
    import time
    time.sleep(10)
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


class ProductViews(PermissionRequiredMixin, LoginRequiredMixin, ListView, ):
    permission_required = "ecoshop.delete_product"
    login_url = "/admin/accounts/login/"
    # import time
    # time.sleep(10)
    template_name = "products.html"
    model = Product
    # paginate_by = 10
    # paginate_orphans = 3
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["products"] = Product.objects.all()
    #     return context


# class ReviewFormView(FormView):
#     template_name = "create_review_product.html"
#     form_class = ProductsReviewsForm
#     success_url = "/ecoshop/comments/"


def create_review(request):
    context = {}

    if request.method == "POST":
        form = ProductsReviewsForm(request.POST)
        form.save()
        # caches["per_cite_cache"].clear()
        if form.is_valid():
            # reviews = ProductsReviewsForm(
            #     **form.cleaned_data
            # )
            # reviews.save()
            return HttpResponseRedirect("/ecoshop/comments/")
    else:
        form = ProductsReviewsForm()

    context["form"] = form
    return render(request, "create_review_product.html", context=context)


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


def create_product_form(request):
    context = {}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        context["form"] = form
        if form.is_valid():
            name = request.POST['name']
            price = request.POST['price']
            description = request.POST['description']
            amount = request.POST['amount']

            category = request.POST["category"]
            if 'image' in request.FILES:
                image = request.FILES["image"]
                product = Product(
                    name=name,
                    price=price,
                    description=description,
                    amount=amount,
                    image=image,
                    category=category
                )
                product.save()
            else:
                generate_photo.delay(
                    name=name,
                    price=price,
                    description=description,
                    amount=amount,
                    category=category
                )
            return redirect("products")
    else:
        form = ProductForm()
        context["form"] = form
    return render(request, "create_product.html", context=context)
