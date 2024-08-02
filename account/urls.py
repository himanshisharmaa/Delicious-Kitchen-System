from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.staticfiles.urls import static
app_name='account'
urlpatterns = [
    path('', login_page , name='login_page'),
    path('register/', register_page , name='register_page'),


]

