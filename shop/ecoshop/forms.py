from django import forms
from django.forms import Textarea

from .models import ProductsReviews, Product


# class ProductsReviewsForm(forms.Form):
#     title = forms.CharField(label="product reviews", max_length=50)
#     description = forms.CharField(label="description", max_length=200)
#     author = forms.CharField(label="author", max_length=20)
#     product =  forms.IntegerField()

class ProductsReviewsForm(forms.ModelForm):
    class Meta:
        model = ProductsReviews
        fields = ['title', 'description', 'author', 'product']
        widgets = {
            "description": Textarea(
                attrs={
                    "cols": 80,
                    "rows": 20,
                    'class': 'special'
                }
            ),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'amount','image','category']
        widgets = {
            "description": Textarea(
                attrs={
                    "cols": 80,
                    "rows": 20,
                    'class': 'special'
                }
            ),
        }