from django.urls import path

from . import views
urlpatterns = [
    path('', views.web),
    path('view', views.slug_autocomplet),
    path('review', views.review_insert)
]
