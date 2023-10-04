from django.urls import path,re_path

from .views import index_ecoshop,info_ecoshop,regular_year_views,data_user_views,goods_catalog

urlpatterns = [
    path("index/", index_ecoshop),
    path("info/<str:ecoshop>/<slug:street>/<int:number>/", info_ecoshop),
    path("data_user_views/", data_user_views),
    path("goods_catalog/", goods_catalog),
    re_path("^openwork/(?P<year>[12][09][89012][0-9])/$", regular_year_views),
]