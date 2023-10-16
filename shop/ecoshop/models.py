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

class Vendor(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    phone= models.CharField(max_length=30,null=True)
    inn = models.PositiveIntegerField()
    product = models.ManyToManyField("Product")

    def __str__(self):
        return self.name

class Shipper(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=30,null=True)
    product = models.ManyToManyField("Product")

    def __str__(self):
        return self.name

class ReviewsProducts(models.Model):
    title = models.CharField(max_length=30)
    description= models.CharField(max_length=300,default="default review")
    author = models.CharField(max_length=30)
    reviews_time =  models.DateField(auto_now_add=True)
    product = models.ForeignKey("Product",on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class PassportShipper(models.Model):
    passport_number = models.PositiveIntegerField()
    passport_series = models.CharField(max_length=5)
    shipper = models.OneToOneField("Shipper",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.passport_number)






