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

    context = {}
    return render(request, 'items/admin.html', context)

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
    cat.delete()
    return redirect('/admin/addCategory/')


def add_brand(request):
    if request.method == 'POST':        
        form = NewBrand(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin/addProduct/')
    else:
        form = NewBrand()
    context = {'add_brand': form}
    return render(request, 'items/add_brand.html', context)

def add_items(request):
    if request.method == 'POST':        
        form = NewProduct(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.slug = slugify(request.POST['name'])
            form.save()
            return redirect('/admin/addVariation/')
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
    


def add_variation(request):
    if request.method == 'POST':
        form_variation = forms.AddVariation(request.POST)
        if form_variation.is_valid():
            form_variation.save()
            return redirect('/admin/addVariationOption/')
    else:
        form_variation = forms.AddVariation()
    context = {"form_variation": form_variation}
    return render(request, 'items/add_variation.html', context)

def add_variationOptions(request):
    if request.method == 'POST':
        form_variation_option = forms.AddVariationOption(request.POST)
        if form_variation_option.is_valid():
            form_variation_option.save()
            return redirect('/home/')
    else:
        form_variation_option = forms.AddVariationOption()
    context = {"form_variation_option": form_variation_option}
    return render(request, 'items/add_variationOptions.html', context)



