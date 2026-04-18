from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q


# Create your views here.
def login_page(request):
    if request.method == 'POST':

        data = request.POST
        mail = data.get('mail', '').strip()
        passwd = data.get('passwd')
        user_record = User.objects.filter(
            Q(username__iexact=mail) | Q(email__iexact=mail)
        ).first()

        if user_record is None:
            messages.error(request, "Invalid email or username")
            return redirect('/')
        else:
            user = authenticate(username=user_record.username, password=passwd)

            if user is None:
                messages.error(request, 'Invalid Password')
                return redirect('/')
            if user.is_superuser:
                login(request, user)
                return redirect('admin/')
            if not user.is_superuser:
                login(request, user)

        return redirect('menu/')

    return render(request, 'account/login.html')


def register_page(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        f_name=data['f_name']
        l_name = data['l_name']
        mail = data['mail']
        passwd = data['passwd']
        rePasswd = data['rePasswd']
        contactNo=data['contact']
        stAddress=data['stAddress']
        landmarks=data['landmarks']
        state = data['state']
        zipCode = data['zipCode']
        completeAddress=stAddress+", "+landmarks+", "+state+", "+zipCode
        user = User.objects.filter(username=mail)

        if user.exists():
            messages.info(request, 'Username Already exists')
            return redirect('/register/')
        if not passwd == rePasswd:
            messages.info(request, "Password Didn't Match")
            return redirect('/register/')

        user_details = User.objects.create(username=mail,first_name=f_name,last_name=l_name,email=mail)
        user_details.set_password(passwd)
        user_details.save()
        UserProfile.objects.create(user=user_details,phone_number=contactNo, address=completeAddress)
        messages.info(request, 'Successfully registered')
        return redirect('/register/')

    return render(request, 'account/register.html')

