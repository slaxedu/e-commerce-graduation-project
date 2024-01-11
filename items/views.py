from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Variation, VariationOption,Brand
from . import forms
from .forms import NewProduct, NewBrand, NewCategory
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import user_passes_test


from django.urls import reverse
# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def admin_panel(request):
    return redirect('add_category')


def add_category(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form_category = NewCategory(request.POST, request.FILES)
        if form_category.is_valid():
            form_category=form_category.save(commit=False)
            form_category.slug = slugify(request.POST['category_name'])
            form_category.save()
            return redirect('/admin/addProduct/')
    else:
        form_category = NewCategory()
    context = {"form_category": form_category,
                "categories": category}
    return render(request, 'items/add_category.html', context)
def update_cat(request, slug):  
    cate = Category.objects.get(slug=slug)
    if request.method == 'POST':
        form = NewCategory(request.POST, request.FILES,instance=cate)
        if form.is_valid():
            form = form.save(commit=False)
            form.slug=slugify(request.POST['category_name'])
            form.save()
            return redirect('/admin/addCategory/')
    else:
        form = NewCategory(instance=cate)
    category = Category.objects.all()
    context = {
        "form_category":form,
        "categories": category
    }
    return render(request, 'items/add_category.html', context)
def delete_cat(request, slug):
    cat = get_object_or_404(Category,slug=slug)
    if request.method == 'POST':
        if request.POST['delete'] == 'Yes':
            if cat.product.exists():
                print("Your Object Can't Delete")
            else:
                cat.delete()
        return redirect('/admin/addCategory')
    return render(request, 'items/delete.html')
def update_brand(request, id):  
    cate = Brand.objects.get(id=id)
    if request.method == 'POST':
        form = NewBrand(request.POST, request.FILES,instance=cate)
        if form.is_valid():
            form.save()
            return redirect('add_brand')
    else:
        form = NewBrand(instance=cate)
    category = Brand.objects.all()
    context = {
        # "form_category":form,
        'add_brand': form,
        "categories": category
    }
    return render(request, 'items/add_brand.html', context)
def delete_brand(request, id):
    cat = get_object_or_404(Brand,id=id)
    if request.method == 'POST':
        if request.POST['delete'] == 'Yes':
            if cat.product.exists():
                print("You Can't Delete ")
            else:
                cat.delete()
        return redirect('add_brand')
    return render(request, 'items/delete.html')


def add_brand(request):
    
    if request.method == 'POST':        
        form = NewBrand(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin/addProduct/')
    else:
        form = NewBrand()
    context = {'add_brand': form,"categories": Brand.objects.all()}
    return render(request, 'items/add_brand.html', context)


def add_items(request):
    if request.method == 'POST':        
        form = NewProduct(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.slug = slugify(request.POST['name'])
            form.count = Product.objects.count()+1
            form.save()
            return redirect('/admin/')
    else:
        form = NewProduct()
    context = {'add_product': form}
    return render(request, 'items/add_items.html', context)
def update_items(request ,slug):
    # item = get_object_or_404(Product, name=name,pk=pk)
    item = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = NewProduct(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            form = form.save(commit=False)
            form.slug = slugify(request.POST['name'])
            
            form.save()
            return redirect('product_items', slug=form.slug)
    else:
        form = NewProduct(instance=item)
    context = {'add_product': form}
    return render(request, 'items/add_items.html',context)
def delete_items(request, slug):
    # item = Product.objects.get(pk=pk)
    item = get_object_or_404(Product,slug=slug)
    item.delete()
    return redirect('/home/')
    

from .forms import AddVariationForm, AddVariationOptionForm

def add_variation(request):
    if request.method == 'POST':
        # form_variation = forms.AddVariation(request.POST)
        form_variation = AddVariationForm(request.POST)
        if form_variation.is_valid():
            form_variation.save()
            return redirect('/admin/addVariationOption/')
    else:
        form_variation = AddVariationForm()
    context = {"form_variation": form_variation}
    return render(request, 'items/add_variation.html', context)

def add_variationOptions(request):
    if request.method == 'POST':
        # form_variation_option = forms.AddVariationOption(request.POST)
        form_variation_option = AddVariationOptionForm(request.POST)
        if form_variation_option.is_valid():
            form_variation_option.save()
            return redirect('/home/')
    else:
        form_variation_option = AddVariationOptionForm()
    context = {"form_variation_option": form_variation_option}
    return render(request, 'items/add_variationOptions.html', context)


from cart_shop.models import Order, OrderItems
from django.db.models import Prefetch

def order_view(request):

    orders_with_items_and_user = Order.objects.order_by('-order_date').prefetch_related(
    'items__product',  # Include product information for each item
    'user'  # Include the user information
    )

    context = {'orders': orders_with_items_and_user}
    
    return render(request, 'items/order_view.html', context)