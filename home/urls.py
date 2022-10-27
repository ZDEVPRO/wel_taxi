from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('driver/', include('home.driver.urls')),
    path('customer/', include('home.customer.urls')),

    path('getorders-driver/', views.getorders_driver, name='getorders-driver'),
    path('getorders-customer/', views.getorders_customer, name='getorders-customer'),

    path('kirish/', views.kirish, name='kirish'),
    path('register-customer/', views.customer_register_request, name='customer-register'),
    path('login-customer/', views.customer_login_view, name='customer-login'),
    path('login-driver/', views.driver_login_view, name='driver-login'),
    path("logout/", views.logout_view, name="logout"),
]
