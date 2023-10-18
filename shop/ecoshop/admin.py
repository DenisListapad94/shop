from .models import Product,ProductsReviews,Vendor,Shipper,Passport,VendorReviews,ShipperReviews

from django.contrib import admin

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductsReviews)
admin.site.register(VendorReviews)
admin.site.register(ShipperReviews)
admin.site.register(Vendor)
admin.site.register(Shipper)
admin.site.register(Passport)