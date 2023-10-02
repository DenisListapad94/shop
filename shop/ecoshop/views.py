import datetime

from django.shortcuts import render
from django.http import HttpResponse


def index_ecoshop(request):
    return HttpResponse("Hello, world. You're at the ecoshop index.")

def info_ecoshop(request,ecoshop,street,number):
    return HttpResponse(f"{ecoshop} on address {street} {number}")

def regular_year_views(request,year):
    return HttpResponse(f"year build is {year}")


def data_views(request):
    return HttpResponse(f"<h1>I am in tag h1</h1>")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>It is now %s.</h1></body></html>" % now
    return HttpResponse(html)