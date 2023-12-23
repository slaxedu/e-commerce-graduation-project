from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    # path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
    path('updata_info/<int:pk>', views.user_update, name='user_update')
]
