import base64
import time

import requests
from celery import shared_task
from django.core.files.base import ContentFile

from .models import Product


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

