from django.urls import path
from home.driver import views

urlpatterns = [
    path('', views.index, name='driver'),
    path('order/<int:id>/', views.order_detail, name='driver-order-detail'),
    path('myorders/', views.myorders, name='driver-myorders'),
    path('close-order/<int:id>/', views.close_order, name='driver-close-order'),
    path('client-in-car/<int:id>/', views.client_in_car, name='driver-client-in-car'),
    path('sucess/<int:id>/', views.success_order, name='driver-success-order'),
]
