from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

app_name='custom_admin'
urlpatterns = [
    path('', adminPanel , name='adminPanel'),
    path('add-items/',add_items,name="add_items"),
    path('view-items/',view_items,name="view_items"),
    path('delete-item/<id>',delete_item,name='delete_item'),
    path('update-item/<id>',update_item,name='update_item'),
    path('manage-orders/',manage_orders,name='manage_orders'),
    path('update-status/<id>', update_status, name='update_status'),
    path('pending-orders/', pending_orders, name='pending_orders'),
    path('completed-orders/', completed_orders, name='completed_orders'),
    path('queries/', show_queries, name='show_queries'),

]

