from django.urls import path,re_path

from .views import index_ecoshop,comments,ReviewFormView,MyView,ProductViews

urlpatterns = [
    path("index/", index_ecoshop,name = "index_ecoshop"),
    # path("info/<str:ecoshop>/<slug:street>/<int:number>/", info_ecoshop),
    path("products/", ProductViews.as_view(),name = "products"),
    path("comments/", comments, name="comments"),
    path("create_review/", ReviewFormView.as_view(), name="create_review"),
    path("my_view/<str:ecoshop>/<slug:street>/<int:number>", MyView.as_view(), name="my_view"),

    # path("goods_catalog/", goods_catalog),
    # re_path("^openwork/(?P<year>[12][09][89012][0-9])/$", regular_year_views),
]