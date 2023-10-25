from django.db import models

from django.db.models.signals import post_save
from django.core.signals import request_finished
from django.dispatch import receiver

class Product(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=["name", "price"]),
            # models.Index(fields=["amount"], name="amount_idx"),
            models.Index(fields=["price","-amount"], name="price_amount_idx"),
        ]

    CATEGORY = [
        ("FR", "Fruit"),
        ("VG", "Vegetable"),
        ("ML", "Milk products"),
        ("MT", "Meat"),
        ("TC", "Tea and coffee"),
        ("FS", "Fish"),
        ("AL", "Alcohol"),
    ]
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100,blank=False,default="perfect products")
    price = models.FloatField()
    amount = models.PositiveIntegerField()
    delivery_date = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY,
    )
    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    phone= models.CharField(max_length=30,null=True)
    product = models.ManyToManyField("Product")


class Passport(models.Model):
    passport_number = models.PositiveIntegerField()
    passport_series = models.CharField(max_length=5)
    person = models.OneToOneField("Person",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.passport_number)

class Vendor(Person):
    inn = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.name

class Shipper(Person):
    personal_discont = models.FloatField(null=True)
    def __str__(self):
        return self.name

class Reviews(models.Model):
    title = models.CharField(max_length=30)
    description= models.CharField(max_length=300,default="default review")
    author = models.CharField(max_length=30)
    reviews_time =  models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class ProductsReviews(Reviews):
    product = models.ForeignKey("Product",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
class VendorReviews(Reviews):
    vendor = models.ForeignKey("Vendor",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
class ShipperReviews(Reviews):
    shipper = models.ForeignKey("Shipper",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")



@receiver(post_save, sender=Person)
def user_created(sender, instance, **kwargs):
    print('signal work')
    # print(sender)
    # print(instance)
    # print(instance.age)
    # hobby = Hobbies.objects.get(id=1)
    # instance.hobbies_set.add(hobby)

post_save.connect(receiver=user_created, sender=Person)





