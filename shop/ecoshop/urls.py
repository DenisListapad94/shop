from django.urls import path,re_path

from .views import index_ecoshop,info_ecoshop,regular_year_views,data_views,current_datetime

urlpatterns = [
    path("index/", index_ecoshop),
    path("info/<str:ecoshop>/<slug:street>/<int:number>/", info_ecoshop),
    path("render_data/", data_views),
    path("current_time/", current_datetime),
    re_path("^openwork/(?P<year>[12][09][89012][0-9])/$", regular_year_views),
]