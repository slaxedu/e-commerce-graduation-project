
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Address, Order, OrderItems
from items.models import Product
import time
# # Filter data after the date
# data = YourModel.objects.filter(date__gte=date_after_3_days)
from django.shortcuts import render, redirect
from .models import Cart
from items.models import Product
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.
@login_required(login_url='/account/register/')
def cart(request):
    items_cart = Cart.objects.all().filter(user=request.user).order_by('id')
    # Get the date after 3 days from now
    date_after_3_days = timezone.now() + timedelta(days=3)
    formatted_date = date_after_3_days.strftime("%A/%d %B")
    total = 0
    add = request.GET.get('quantity', 1)
    product_slug = request.GET.get('product', '')
    if add != 1 and product_slug != '':
        pro = Product.objects.get(slug=product_slug)
        item_cart = Cart.objects.filter(product=pro.id).update(quantity=add)
    j = 0
    for i in items_cart:
        total += i.product.price * i.quantity
        j +=1
    
    
    if request.method == 'POST':
        locat = request.POST['location']
        phone = request.POST['phone']
        city = request.POST['city']
        street = request.POST['street']
        if locat:
            address = locat
        else:
            gover = request.POST['governorate']
            address = f"EG-{gover}-{city}-{street}"
        if items_cart:
            add_model =Address.objects.create(
                address=address
            )
            order = Order.objects.create(
                user=request.user,
                total_price=total,
                order_date=timezone.now(),
                shoping_address = add_model,
            )
            for cart in items_cart:
                # order_items = OrderItems.objects.create(
                #     product = cart.product,
                #     quantity = cart.quantity,
                # )
                quant = Product.objects.get(id=cart.product.id).quantity_in_stock
                product = Product.objects.filter(id=cart.product.id).update(quantity_in_stock=quant-1)
                ord_item = OrderItems.objects.create(
                    order=order,product=cart.product,quantity=cart.quantity)

            # order = Order.objects.create(
            #     user=request.user,
            #     product=order_items,
            #     total_price=total,
            #     order_date=timezone.now(),
            #     shoping_address = add_model,
            # )
            message = f'It Will Arrive: {formatted_date}\n'
            for item in items_cart:
                message+= f'Name: {item.product}\nPrice: {item.product.price}\n'
            subject = 'Your order has been confirmed'
            message += f"Total Price: {total}" 
            from_email = 'your_email@example.com'
            # recipient_list = [ request.user.email, "egyptisyouth@gmail.com"]
            recipient_list = [  "egyptisyouth@gmail.com"]
            try:
                send_mail(subject, message, from_email, recipient_list)
            except:
                print("email Not Found")
            items_cart.delete()
            time.sleep(1)
            return redirect('home')
    last_order = Order.objects.filter(user=request.user).order_by('-id').first()
    order_items = ''
    if last_order:
        order_items = OrderItems.objects.filter(order=last_order)
    print(last_order)
    context = {
        'order_last': last_order,
        'order_items': order_items,
        'items_cart': items_cart,
        'total': total,
        'number_product': j,
        'date': formatted_date,
    }
    return render(request, 'cart_shop/cart.html',context)

@login_required(login_url='/account/register/')
def cart_detele(request, slug):
    try:
        item_cart = Cart.objects.filter(user=request.user).filter(product__slug=slug)
        time.sleep(5)
        item_cart.delete()
    except:
        print('no items')
    return redirect('cart')

