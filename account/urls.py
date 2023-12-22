from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    # path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # path('log_out/', views.log_out, name='log_out'),
    path('updata_info/<int:pk>', views.user_update, name='user_update')
]
