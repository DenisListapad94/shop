from django.db import models




class Product(models.Model):
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










