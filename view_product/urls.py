from django.urls import path
from . import views

import re
urlpatterns = [
    path('home/', views.home, name='home'),
    path('product/<str:slug>/', views.product_items, name='product_items'),
    path('category/<str:slug>/', views.categ_home, name='category_home'),
    # path('product/'+re.sub(r"\W?", '-','<str:name>/'), views.product_items, name='product_items'),
    # path('product/'+'r^(?P<college_id>[0-9]+)/$', views.product_items, name='product_items'),
    path('product/<str:slug>/review', views.review, name='all_comment'),
]
