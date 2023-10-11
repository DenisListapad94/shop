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
    vendor = models.CharField(max_length=30)
    amount = models.PositiveIntegerField()
    delivery_date = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY,
    )
    def __str__(self):
        return self.name






