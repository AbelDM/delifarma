from django.urls import path
from .views import listaUsuario, listaProduct, listaCustomer, listaOrders, listaFeedback, detalleProduct, \
    detalleUsuario, detalleCustomer, detalleOrders, detalleFeedback
from rest_framework.authtoken import views

urlpatterns = [
    path('users/', listaUsuario.as_view(), name='user_list'),
    path('users/<int:pk>', detalleUsuario.as_view(), name='user_detalle'),
    path('products/', listaProduct.as_view(), name='product_list'),
    path('products/<int:pk>', detalleProduct.as_view(), name='product_detalle'),
    path('customer/', listaCustomer.as_view(), name='customer_list'),
    path('customer/<int:pk>', detalleCustomer.as_view(), name='customer_detalle'),
    path('orders/', listaOrders.as_view(), name='orders_list'),
    path('orders/<int:pk>', detalleOrders.as_view(), name='orders_detalle'),
    path('feedback/', listaFeedback.as_view(), name='feedback_list'),
    path('feedback/<int:pk>', detalleFeedback.as_view(), name='feedback_detalle'),

]


