from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    #path('login-user/', views.login_user, name = 'login'),
    path('logout-user/', views.logout_user, name = 'logout'),
    path('register-user/', views.register_user, name = 'register'),
    path('record/<int:pk>', views.customer_record, name = 'record'),
]
