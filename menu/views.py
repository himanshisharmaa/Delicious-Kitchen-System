from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from custom_admin.models import *
from django.conf import settings
from .models import *
import json
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account.models import UserProfile
import razorpay
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
@login_required(login_url='/')
def menu_page(request):
    querySet=Menu.objects.all()
    if request.GET.get('search'):
        item_name=request.GET.get('search')
        querySet= Menu.objects.filter(item_name__icontains=item_name)
    elif request.GET.get('close'):
        return redirect('/menu/')
    queryset = querySet.order_by('-item_type')
    context={'items_display':queryset}
    return render(request,'menu/menu_display.html',context)


@login_required(login_url='/')
def add_to_cart(request):
    user_details = request.user
    querySet = UserProfile.objects.get(user=user_details)
    context = {'user_details': querySet}
    return render(request,'menu/add_to_cart.html',context)

def contact(request):
    if request.method=="POST":
        data=request.POST

        name=data.get('name')
        mail_id = data.get('mail_id')
        subject=data.get('subject')
        msg=data.get('message')
        user=request.user
        print(user)
        add_query=ContactUs.objects.create(user=user,nameOfUser=name,email_id=mail_id,subjectOfQuery=subject,queryMessage=msg)
        add_query.save()
        messages.info(request,'Your query has been sent successfully!! We will get back to you as soon as possible')
        return redirect('/menu/contact-us/')
    return render(request,'menu/contact.html')


def about(request):
    return render(request,'menu/about.html')

@login_required(login_url='/')
def showProfile(request):
    user_details=request.user
    querySet=UserProfile.objects.get(user=user_details)
    context={'user_details':querySet}
    return render(request,'menu/profile.html',context)

def logout_page(request):
    logout(request)
    return redirect('/')


@csrf_exempt
def make_payment(request):
    print(request.GET)
    amt=int(request.GET['total_amt'])
    print(amt)
    client=razorpay.Client(auth=(settings.KEY,settings.SECRET))

    payment=client.order.create({'amount':amt*100,'currency':'INR','payment_capture':1})

    context={'payment':payment}
    return JsonResponse(context)
def liveSearchForm(request):
    if 'term' in request.GET:
        qs=Menu.objects.filter(item_name__icontains=request.GET.get('term'))
        data = []
        for items in qs:
            data.append(items.item_name)
        res=data
    # if request.method=='POST':
    #     item_name=request.POST.get('item_name')
    #     queryset=Menu.objects.filter(item_name__icontains=item_name)
    #     if len(queryset)>0 and len(item_name)>0:
    #         data=[]
    #         for items in queryset:
    #             data.append(items.item_name)
    #         res=data
    #     else:
    #         res="No item Found.."
        return JsonResponse(res,safe=False)
    return JsonResponse({})

def order_complete(request):
    if request.method == 'POST':
        fullName = request.POST.get('fullName')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        email = request.POST.get('email')
        phone_num = request.POST.get('phone_num')
        cart_items = request.POST.get('cart_items')
        totalPrice = request.POST.get('totalPrice')
        payment_id = request.POST.get('payment_id')
        order_id = request.POST.get('order_id')
        order_signature = request.POST.get('order_signature')
        user = request.user
        full_address=f'{address} {city} ,{zip}'
        order_time=timezone.now()
        Order.objects.create(
            user=user,
            fullName=fullName.capitalize(),
            address=full_address.capitalize(),
            email_id=email,
            ph_num=phone_num,
            cart_items=cart_items,
            totalAmount=totalPrice,
            is_paid=True,
            payment_id=payment_id,
            order_id=order_id,
            order_placed_time = order_time

        )
        OrderStatus.objects.create(
            order_id=order_id,
            time_status=order_time

        )
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def success(request):
    orders = Order.objects.filter(user=request.user.id)
    latest_order = orders.order_by('-order_placed_time').first()
    context={'order_details':latest_order}

    return render(request,'menu/success.html',context)
def show_orders(request):
    orders = Order.objects.filter(user=request.user.id)
    latest_order = orders.order_by('-order_placed_time')
    for item in latest_order:
        item.cart_items = json.loads(item.cart_items)
        print(type(item.cart_items))
    context = {'order_details': latest_order}
    return render(request,'menu/order.html',context)

def order_details(request,id):
    order_items=Order.objects.get(order_id=id)
    order_items.cart_items=json.loads(order_items.cart_items)
    order=OrderStatus.objects.filter(order_id=id)
    data={}
    for i in order:
        status=i.order_status.replace(" ","")
        print(f'{status} : {i.time_status}')
        data[status] = i.time_status
    context={'order_data':data,'order':order_items}
    return render(request,'menu/order_details.html',context)