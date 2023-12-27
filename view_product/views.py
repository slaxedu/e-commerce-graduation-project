from django.shortcuts import render, redirect, get_list_or_404
from items.models import Category, Product, Brand, Review, Comment
from account.models import CustomUser
from django.db.models import Q
from cart_shop.models import Cart
# from items.forms import ReviewForm
from django.core.paginator import Paginator
from django.db.models import Avg, Max, Min, Count
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .models import ClickCount


def home(request):
    number = 0
    if request.user:
        number = Cart.objects.all().filter(user=request.user.id).count()
    product = Product.objects.all()
    category = Category.objects.all()
    # product = Product.objects.all()
    prod_min = Product.objects.order_by('price').first()
    prod_max = Product.objects.order_by('price').last()
    # brand = Brand.objects.all()
    query = request.GET.get('q', '')
    vector = SearchVector('name')
    search_query = SearchQuery(query)
    categ = request.GET.get('category', 0)
    br = request.GET.get('br', 0)
    def cat_return(categ):
        if categ != 0:
            return categ
    cat_id = cat_return(categ)
    if query:
        product = product.filter(Q(name__icontains=query)|Q(description__icontains=query))
        # product = product.filter(name__search=query)
        # product =  product.annotate(rank=SearchRank(vector, search_query)).filter(rank__gte=.3).order_by('-rank')
    if categ:
        product = product.filter(category_id_id = categ)
        # product_p = p.filter(category_id_id = categ)
        if br:
            product= product.filter(category_id_id = categ).filter(brand_id_id = br)
    if br:
        product = product.filter(brand_id_id = br)
    p = Paginator(product, 28)
    page = request.GET.get('page')
    product_p = p.get_page(page)
    brand = Brand.objects.all()
    context = {"category": category[0:4],
                "cat_id": cat_id ,
                "category_all": category[0:15],
                "brand": brand,
                'q': query,
                "product": product_p,
                "number_product": number,
                }
    return render(request, 'view_product/home.html', context)

def categ_home(request, slug):
    number = 0
    if request.user:
        number = Cart.objects.all().filter(user=request.user.id).count()
    category = Category.objects.all()
    product=Product.objects.all()
    try:
        cate = Category.objects.get(slug=slug)
        product = Product.objects.filter(category_id=cate.id)
    except:
        cate = category
        cate.slug = ''
    query = request.GET.get('q', '')
    br = request.GET.get('br', 0)
    
    # if request.method == 'GET':
    #     min_price = request.GET.get('min', '')
    #     max_price = request.GET.get('max', '')
    #     try:
    #         min_price = int(min_price)
    #         max_price = int(max_price)
    #         product  = Product.objects.filter(price=min_price) and Product.objects.filter(price=int(max_price))
            
            
    #     except:
    #         # product  = Product.objects.filter(price=10000) and Product.objects.filter(price=10000)
    #         print('nothing')
    #     print(f'######################### min_price {min_price}')
    #     print(f'######################### max_price {max_price}')
        
    

    if query:
        product = product.filter(Q(name__icontains=query)|Q(description__icontains=query))
    if br:
        product = product.filter(brand_id_id = br)

    p = Paginator(product, 28)
    page = request.GET.get('page')
    product_p = p.get_page(page)
    # product_p = product
    brand = []
    for i in product:
        if i.brand_id and {'name':i.brand_id,'id':i.brand_id.id} not in brand:
            brand.append({'name': i.brand_id,
                            'id': i.brand_id.id})
    
    context = {"category": category[0:4],
                "cat_id": '' ,
                "category_all": category[0:15],
                "brand": brand[0:5],
                'q': query,
                "product": product_p,
                "slug": cate.slug,
                "number_product": number,
                }
    
    return render(request, 'view_product/home.html', context)



def product_items(request, slug):
    product_item = Product.objects.get(slug=slug)
    comment = Review.objects.filter(product_id=product_item.id).order_by("-id")#.distinct("comment")
    num_comment = Review.objects.filter(product_id=product_item.id).count()
    random_object = Product.objects.filter(category_id=product_item.category_id).order_by('?')[0:4]
    product = request.GET.get('add_cart', '')
    b = request.GET.get('go', '')
    try:
        user = request.user
        user = CustomUser.objects.get(id=user.id)
        product_cart = Product.objects.get(slug=product)
        cart = Cart.objects.get_or_create(
            user = user,
            product = product_cart,
            quantity=1
        )
        if b == 'buy':
            return redirect('/cart/')
    except:
        print("nothing")
    
    if request.method == 'POST':
        message = request.POST['message']
        rate = request.POST.get('rating', False) or 0
        if request.user.is_authenticated:
            if message != '' or rate != 0:
                
                com = Comment.objects.create(
                        comment = message
                    )
                rev =Review.objects.filter(product=product_item).filter(user=request.user)
                if rev :
                    if message != '':
                        review = Review.objects.create(
                            user = request.user,
                            product = product_item,
                            rate  = rate,
                            comment = com,
                        )
                    review = rev.update(rate=rate)
                else:
                    review = Review.objects.create(
                        user = request.user,
                        product = product_item,
                        rate  = rate,
                        comment = com,
                    )
        else:
            return redirect('register')
    number = 0
    if request.user:
        number = Cart.objects.all().filter(user=request.user.id).count()
    if num_comment > 0:
        reviews_stats = Review.objects.filter(product=product_item.id).aggregate(
            average_rating=Avg('rate'),
            max_rating=Max('rate'),
            min_rating=Min('rate'),
        )

        average_rating = reviews_stats['average_rating']
        max_rating = reviews_stats['max_rating']
        min_rating = reviews_stats['min_rating']
    else:
        max_rating = 0
        min_rating = 0
        average_rating=0



    
    click = ClickCount.objects.get_or_create(product=product_item)
    
    if click:
        click = ClickCount.objects.filter(product=product_item)
        
        for x in click:
            print(x)
            click.update(count=x.count+1)



    context = {
        "comments": comment[0:3],
        "num_comment": num_comment,
        "product_item": product_item,
        "related_product": random_object,
        "number_product": number,
        "max": max_rating,
        "min": min_rating,
        "average": round(average_rating, 2),
    }
    return render(request, 'view_product/product.html', context)
def review(request, slug):
    number = Cart.objects.all().filter(user=request.user.id).count()
    product_item = Product.objects.get(slug=slug)
    comment = Review.objects.filter(product_id=product_item.id).order_by("-id")
    num_comment = Review.objects.filter(product_id=product_item.id).count()
    if request.method == 'POST':
        message = request.POST['message']
        rate = request.POST.get('rating', False) or 0
        if message != '' or rate != 0:
            
            com = Comment.objects.create(
                    comment = message
                )
            
            rev =Review.objects.filter(product=product_item).filter(user=request.user)
            if rev :
                if message != '':
                    review = Review.objects.create(
                        user = request.user,
                        product = product_item,
                        rate  = rate,
                        comment = com,
                    )
                review = rev.update(rate=rate)
            else:
                review = Review.objects.create(
                    user = request.user,
                    product = product_item,
                    rate  = rate,
                    comment = com,
                )
    number = 0
    if request.user:
        number = Cart.objects.all().filter(user=request.user.id).count()

    
    reviews_stats = Review.objects.filter(product_id=product_item.id).aggregate(
        average_rating=Avg('rate'),
        max_rating=Max('rate'),
        min_rating=Min('rate'),
    )

    # Now you can access the statistics
    average_rating = reviews_stats['average_rating']
    max_rating = reviews_stats['max_rating']
    min_rating = reviews_stats['min_rating']
    context = {
        "comments": comment,
        "num_comment": num_comment,
        "product_item": product_item,
        "number_product": number,
        "max": max_rating,
        "min": min_rating,
        "average": round(average_rating,2),
    }
    return render(request, 'view_product/review.html', context)
