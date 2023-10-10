from django.urls import path,re_path

from .views import index_ecoshop,products,comments

urlpatterns = [
    path("index/", index_ecoshop,name = "index_ecoshop"),
    # path("info/<str:ecoshop>/<slug:street>/<int:number>/", info_ecoshop),
    path("products/", products,name = "products"),
    path("comments/", comments, name="comments"),
    # path("goods_catalog/", goods_catalog),
    # re_path("^openwork/(?P<year>[12][09][89012][0-9])/$", regular_year_views),
]