from django.urls import path
from . import views
urlpatterns = [
    # path('', views.get_product),
    path('', views.main, name='main'),
    path('another/', views.test),
    

]