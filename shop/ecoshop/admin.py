from .models import Product,ReviewsProducts,Vendor,Shipper,PassportShipper

from django.contrib import admin

# Register your models here.
admin.site.register(Product)
admin.site.register(ReviewsProducts)
admin.site.register(Vendor)
admin.site.register(Shipper)
admin.site.register(PassportShipper)