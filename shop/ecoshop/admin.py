from django.db.models import F

from .models import Product,ProductsReviews,Vendor,Shipper,Passport,VendorReviews,ShipperReviews,Person
from django.utils.safestring import mark_safe
from django.contrib import admin

@admin.action(description="Up price selected instance on 10")
def price_up_10(modeladmin, request, queryset):
    # for query in queryset:
    #     query.price += 10
    #     query.save()
    queryset.update(price=F("price") +10)
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     pass

# class PersonInline(admin.StackedInline):
#     model = Person

class ProductsReviewsInline(admin.StackedInline):
    model = ProductsReviews

class ProductPerson_m2m_Inline(admin.StackedInline):
    model = Person.product.through



@admin.display(description='фото')
def get_html_photo(objects):
    if objects.image:
        return mark_safe(f'<img src={objects.image.url} width=50>')


class ProductAdmin(admin.ModelAdmin):
    view_on_site = True
    save_on_top = True
    list_display = ["name", "price", "amount","category","view_description",get_html_photo]
    list_display_links = ["name", "view_description",]
    list_editable = ["price", "amount"]
    readonly_fields = ["category"]
    ordering = ["-price"]
    search_fields = ["category","name",]
    # list_filter = ["name", "price", "amount"]
    # fieldsets = [
    #     (
    #         None,
    #         {
    #             "fields": ["name", "price"],
    #         },
    #     ),
    #     (
    #         "Advanced options",
    #         {
    #             "classes": ["collapse"],
    #             "fields": ["amount", "category"],
    #         },
    #     ),
    # ]
    # fields = [("name", "price"),"amount","category"]
    # exclude = ["price"]
    @admin.display(description="Описание")
    def view_description(self, obj):
        return obj.description[:10]

    inlines = [
        # PersonInline,
        ProductsReviewsInline, # one to many
        ProductPerson_m2m_Inline # many to many
    ]
    actions = [price_up_10]



class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "email"]




# Register your models here.
admin.site.register(Product,ProductAdmin)

admin.site.register(Person,PersonAdmin)



admin.site.register(ProductsReviews)
admin.site.register(VendorReviews)
admin.site.register(ShipperReviews)
admin.site.register(Vendor)
admin.site.register(Shipper)
admin.site.register(Passport)