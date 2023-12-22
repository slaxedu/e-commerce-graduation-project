from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart, name='cart'),
    # path('', views.order, name='order'),
    path('<slug:slug>', views.cart_detele, name='cart_detele'),
]
