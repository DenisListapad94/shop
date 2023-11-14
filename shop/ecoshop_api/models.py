from django.db import models

class ProductApi(models.Model):
    name = models.CharField(max_length=30,verbose_name="Название")
    price = models.FloatField(verbose_name="Стоимость")
    amount = models.PositiveIntegerField(verbose_name="Количество")
