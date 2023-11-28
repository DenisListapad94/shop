import base64
import time

import requests
from celery import shared_task
from celery.schedules import crontab
from django.core.files.base import ContentFile

from .models import Product

from django.core.mail import send_mail

# from ..shop.celery import app
#
#
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
#
#     # Calls test('hello') every 30 seconds.
#     # It uses the same signature of previous task, an explicit name is
#     # defined to avoid this task replacing the previous one defined.
#     sender.add_periodic_task(30.0, test.s('hello'), name='add every 30')
#
#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)
#
#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )



@shared_task
def send_msg_for_mail(email):
    send_mail(
        "Рассылка товаров",
        "Мы будем отправлять вам актуальную информацию",
        'den72414@gmail.com',
        [email],
        fail_silently=False,
    )



@shared_task
def summa(x, y):
    time.sleep(10)
    print(x + y)


@shared_task
def mul(x, y):
    return x * y


@shared_task
def generate_photo(name, price, description, amount, category):
    response = requests.post(
        'https://bf.dallemini.ai/generate',
        json={'prompt': description}
    )
    data = base64.b64decode(response.json()['images'][0])
    image = ContentFile(data, name='hello.png')
    Product.objects.create(
        name=name,
        price=price,
        description=description,
        amount=amount,
        category=category,
        image=image
    )

