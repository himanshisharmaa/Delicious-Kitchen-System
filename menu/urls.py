from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.staticfiles.urls import static
app_name='menu'
urlpatterns = [
    path('', menu_page , name='menu_page'),
    path('cart/',add_to_cart,name='add_to_cart'),
    path('contact-us/',contact,name='contact'),
    path('about-us/',about,name='about'),
    path('logout/',logout_page,name="logout_page"),
    path('profile/',showProfile,name="showProfile"),
    path('search/',liveSearchForm,name='liveSearchForm'),
    path('make-payments/',make_payment,name='make_payment'),
    path('success/',success,name='success'),
    path('order-complete/',order_complete,name='order_complete'),
    path('orders/',show_orders,name='order'),
    path('order-<id>/',order_details,name='order_details'),
]
