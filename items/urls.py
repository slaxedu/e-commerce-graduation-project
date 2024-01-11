from django.urls import path
from . import views


urlpatterns = [
    path('order/', views.order_view, name='order_view' ),
    path('', views.admin_panel, name='admin_panel'),
    path('addProduct/', views.add_items, name='add_product'),
    # path('deleteProduct/<str:name>/<int:pk>', views.delete_items, name='delete_product' ),
    path('addBrand/', views.add_brand, name='add_brand'),
    path('addCategory/', views.add_category, name='add_category'),
    path('editCategory/<str:slug>/', views.update_cat, name='edit_category'),
    path('<str:slug>/', views.delete_cat, name='delete_category'),
    path('editBrand/<int:id>/', views.update_brand, name='edit_brand'),
    path('deleteBrand/<int:id>/', views.delete_brand, name='delete_brand'),
    path('addVariation/', views.add_variation, name='add_variation'),
    path('addVariationOption/', views.add_variationOptions, name='addvariationOption'),
    path('editProduct/<str:slug>/', views.update_items, name='edit_product'),
    path('delete/<str:slug>/', views.delete_items, name='delete_product' ),
]

