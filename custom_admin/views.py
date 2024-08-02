from django.shortcuts import render,redirect
from .models import Menu
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from menu.models import *
from django.db.models import Q
from collections import Counter
from django.db.models import Sum
from django.db.models import Count
import json
from django.utils import timezone
# Create your views here.
@login_required(login_url='/')
def adminPanel(request):
    received_orders = Order.objects.filter(order_status='Received')

    # Format the order details for display in the table
    order_details = []
    for order in received_orders:
        order_details.append({
            'order_id': order.order_id,
            'user_name': order.fullName,
            'timestamp': order.order_placed_time
        })
    total_earnings = Order.objects.filter(is_paid=True).aggregate(total=models.Sum('totalAmount'))['total'] or 0

    # Calculate total number of pending orders
    pending_orders = Order.objects.filter( ~Q(order_status='Delivered')).count()

    # Calculate total number of completed orders
    completed_orders = OrderStatus.objects.filter(order_status='Delivered').count()
    orders = Order.objects.all()

    # Extract menu items and quantities from each order's cart
    menu_items_count = Counter()
    for order in orders:
        cart_items = json.loads(order.cart_items)
        for item_id, item_data in cart_items.items():
            menu_items_count[item_data['item_name']] += int(item_data['quantity'])

    # Sort menu items by frequency
    sorted_menu_items = sorted(menu_items_count.items(), key=lambda x: x[1], reverse=True)[:5]

    # Extract menu item names and counts for chart data
    menu_item_names = [item[0] for item in sorted_menu_items]
    menu_item_counts = [item[1] for item in sorted_menu_items]

    context = {
        'income': total_earnings,
        'pending_total': pending_orders,
        'completed_total': completed_orders,
        'menu_item_names': menu_item_names,
        'menu_item_counts': menu_item_counts,
        'order_details': order_details,
        }
    return render(request,'custom_admin/dashboard.html',context)
@login_required(login_url='/')
def add_items(request):
    if request.method=='POST':
        data=request.POST
        item_name=data.get('item_name')

        item_price = data.get('item_price')
        num_pieces=data.get('num_pieces')
        item_description = data.get('item_description')
        item_image=request.FILES['item_image']
        item_type = data.get('item_type')
        Menu.objects.create(item_name=item_name,item_price=item_price,num_pieces=num_pieces,item_description=item_description,item_image=item_image,item_type=item_type)
        messages.info(request,"Successfully Added!!")
        return redirect('/admin/add-items/')
    return render(request,'custom_admin/add_items.html')
@login_required(login_url='/')
def view_items(request):
    queryset=Menu.objects.all()
    context={'menu_items':queryset}
    return render(request,'custom_admin/view_items.html',context)
@login_required(login_url='/')
def delete_item(request,id):
    Menu.objects.get(id=id).delete()
    return redirect('/admin/view-items/')
@login_required(login_url='/')
def update_item(request,id):
    queryset=Menu.objects.get(id=id)
    if request.method=="POST":
        data = request.POST
        item_name = data.get('item_name')

        item_price = data.get('item_price')
        num_pieces = data.get('num_pieces')
        item_description = data.get('item_description')
        item_image = request.FILES.get('item_image')
        item_type = data.get('item_type')
        print(request.POST)
        queryset.item_name=item_name

        queryset.item_price=item_price
        queryset.num_pieces = num_pieces
        queryset.item_description=item_description
        if item_image:
            queryset.item_image=item_image
        if not item_type=='Select Item Type':
            print("Enter")
            queryset.item_type=item_type
        queryset.save()
        return redirect('/admin/view-items/')
    context={'item':queryset}
    return render(request,'custom_admin/update_item.html',context)

def manage_orders(request):
    querySet=Order.objects.all()
    for i in querySet:
        i.cart_items=json.loads(i.cart_items)

    context={'order_details':querySet}

    return render(request,'custom_admin/manage_orders.html',context)

def update_status(request,id):
    if request.method=="POST":
        order_status=request.POST.get('status')
        print(order_status)
        order=Order.objects.get(order_id=id)
        order.order_status=order_status
        order.order_complete_time=timezone.now()
        order.save()
        OrderStatus.objects.create(
            order_id=id,
            order_status=order_status,
            time_status=timezone.now()
        )
        messages.success(request,"Order Status Updated Successfully")
        return redirect('/admin/manage-orders/')
    return redirect('/admin/manage-orders/')



def pending_orders(request):
    querySet = Order.objects.all()
    for i in querySet:
        i.cart_items = json.loads(i.cart_items)
    context = {'order_details': querySet}
    return render(request,'custom_admin/pending_orders.html',context)

def completed_orders(request):
    querySet = Order.objects.all()
    for i in querySet:
        i.cart_items = json.loads(i.cart_items)
    context = {'order_details': querySet}
    return render(request,'custom_admin/completed_orders.html',context)

def show_queries(request):
    context={'queries':ContactUs.objects.all()}
    return render(request,'custom_admin/query.html',context)

def logout_page(request):
    logout(request)
    return render(request,'account/login.html')