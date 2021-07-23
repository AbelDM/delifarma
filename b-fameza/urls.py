from django.contrib import admin
from django.urls import path, include
from fameza import views1
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authtoken import views
from api.views import Login, Cerrar
from fameza import Soap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views1.home_view, name=''),
    path('api/', include(('api.urls', 'api'))),
    path('Soap/', Soap.consulta()),
    path('apigenerador/', views.obtain_auth_token),
    path('inicio/', Login.as_view(), name='login'),
    path('Cerrar/', Cerrar.as_view()),
    path('afterlogin', views1.afterlogin_view, name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='fameza/logout.html'), name='logout'),
    path('aboutus', views1.aboutus_view),
    path('contactus', views1.contactus_view, name='contactus'),
    path('search', views1.search_view, name='search'),
    path('send-feedback', views1.send_feedback_view, name='send-feedback'),
    path('view-feedback', views1.view_feedback_view, name='view-feedback'),

    path('adminclick', views1.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='fameza/adminlogin.html'), name='adminlogin'),
    path('admin-dashboard', views1.admin_dashboard_view, name='admin-dashboard'),

    path('view-customer', views1.view_customer_view, name='view-customer'),
    path('delete-customer/<int:pk>', views1.delete_customer_view, name='delete-customer'),
    path('update-customer/<int:pk>', views1.update_customer_view, name='update-customer'),

    path('admin-products', views1.admin_products_view, name='admin-products'),
    path('admin-add-product', views1.admin_add_product_view, name='admin-add-product'),
    path('delete-product/<int:pk>', views1.delete_product_view, name='delete-product'),
    path('update-product/<int:pk>', views1.update_product_view, name='update-product'),

    path('admin-view-booking', views1.admin_view_booking_view, name='admin-view-booking'),
    path('delete-order/<int:pk>', views1.delete_order_view, name='delete-order'),
    path('update-order/<int:pk>', views1.update_order_view, name='update-order'),

    path('customersignup', views1.customer_signup_view),
    path('customerlogin', LoginView.as_view(template_name='fameza/customerlogin.html'), name='customerlogin'),
    path('inicio-cliente', views1.customer_home_view, name='customer-home'),
    path('my-order', views1.my_order_view, name='my-order'),
    path('my-profile', views1.my_profile_view, name='my-profile'),
    path('edit-profile', views1.edit_profile_view, name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>', views1.download_invoice_view, name='download-invoice'),

    path('add-to-cart/<int:pk>', views1.add_to_cart_view, name='add-to-cart'),
    path('carrito', views1.cart_view, name='carrito'),
    path('remove-from-cart/<int:pk>', views1.remove_from_cart_view, name='remove-from-cart'),
    path('customer-address', views1.customer_address_view, name='customer-address'),
    path('payment-success', views1.payment_success_view, name='payment-success'),

]
