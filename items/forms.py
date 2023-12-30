from django import forms
from .models import Product, Category, Variation, VariationOption, Brand, Review

class NewCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
    slug = forms.CharField(required=False)
    category_name=forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Category Name',
    'class': 'form-control first-input',
    }))

class NewBrand(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"
    name=forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Brand Name',
    'class': 'form-control first-input',
    }))

class NewProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ('name', 'description', 'price',)
    slug = forms.CharField(required=False)
    name=forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Product Name',
    'class': 'form-control first-input',
    }))
    description=forms.CharField(widget=forms.Textarea(attrs={
    'placeholder': 'Description',
    'class': 'form-control first-input',
    }))
    price=forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Price',
    'class': 'form-control last-input',
    }))

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ('rate', 'comment')


class AddVariationForm(forms.ModelForm):
    class Meta:
        model = Variation
        fields = "__all__"
    name=forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Name',
    'class': 'form-control last-input',
    }))
    
    

class AddVariationOptionForm(forms.ModelForm):
    class Meta:
        model = VariationOption
        fields = "__all__"
    value=forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Value',
    'class': 'form-control last-input',
    }))
