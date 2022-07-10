from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from shop.models import Basket, Category, Order, Product

def user_login(request):
    categories = Category.objects.order_by("id")[0:5]
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('/profile/')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form, 'cats': categories})

def user_register(request):
    categories = Category.objects.order_by("id")[0:5]
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = User.objects.create(username=data['username'], email=data['email'])
                user.set_password(data['password'])
                user.save()
                Basket.objects.create(user=user).save()
                return redirect('/login/')
            except IntegrityError:
                return HttpResponse('Username and email must be unique')
        else:
            return HttpResponse('Form filled incorrectly')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form, 'cats': categories})

def profile(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user).order_by("-id")
        categories = Category.objects.order_by("id")[0:5]
        return render(request, 'account/profile.html', {'cats': categories, 'orders':orders})
    else:
        return HttpResponseRedirect('/login/')
