from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import CallbackForm, RatingForm
from django.db import IntegrityError
from shop.models import Basket, Callback, Category, Order, Product, Rating, Seller


def index(request):
    categories = Category.objects.order_by("id")[0:5]
    items = Product.objects.order_by("-id")[0:4]
    big_items = Product.objects.order_by("-id")[0:8]
    more_cats = Category.objects.order_by("id")[5:10]

    return render(request, 'pages/index.html', context={'cats': categories, 'items': items, 'more_cats': more_cats, 'big_items': big_items})


def addToBasket(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            basket = Basket.objects.get(user=user)
            new_product = Product.objects.get(id=pk)
            basket_products = basket.products.all()
            if new_product not in basket_products:
                basket.products.add(new_product)
                basket.subtotal += new_product.price
                basket.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/')


def products(request):
    products_info = Product.objects.all()

    categories = Category.objects.order_by("id")[0:5]
    context = {'cats': categories, 'products': products_info}
    return render(request, 'pages/products.html', context=context)


def product(request, pk):
    product_info = Product.objects.get(id=pk)
    if request.method == 'POST':
        try:
            form = RatingForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                print(data)
                rating_data = Rating.objects.create(
                    product=product_info, creator=request.user, title=data['title'], text=data['description'] )
                rating_data.save()
            else:
                return HttpResponse('Form filled incorrectly')
            return HttpResponseRedirect(f'/products/{pk}')
        except IntegrityError:
            return HttpResponseRedirect(f'/products/{pk}')
    rating_data = Rating.objects.filter(product=product_info)
    categories = Category.objects.order_by("id")[0:5]
    product_cats = Category.objects.filter(product=product_info)
    context = {'cats': categories, 'product': product_info,
               'product_cats': product_cats, 'form': RatingForm, 'ratings': rating_data}
    return render(request, 'pages/product.html', context=context)


def categories(request):
    categories = Category.objects.order_by("id")
    context = {'cats': categories[0:5], 'categories': categories}
    return render(request, 'pages/category.html', context=context)


def category(request, pk):
    categories = Category.objects.order_by("id")[0:5]
    cat = Category.objects.get(id=pk)
    products_info = Product.objects.filter(category=cat)
    context = {'cats': categories, 'category': cat, 'products': products_info}
    return render(request, 'pages/category.html', context=context)


def seller(request, pk):
    seller_info = Seller.objects.get(id=pk)
    categories = Category.objects.order_by("id")[0:5]
    products_info = Product.objects.filter(seller=seller_info)
    context = {'cats': categories,
               'seller': seller_info, 'products': products_info}
    return render(request, 'pages/seller.html', context=context)


def callback(request):
    categories = Category.objects.order_by("id")[0:5]
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            callback_data = Callback.objects.create(
                phone=data['phone'], name=data['name'])
            callback_data.save()
            return redirect('/')
        else:
            return HttpResponse('Form filled incorrectly')
    else:
        form = CallbackForm()
    return render(request, 'pages/callback.html', {'form': form, 'cats': categories})


def removeItemFromBasket(request, pk):
    product = Product.objects.get(id=pk)
    basket = Basket.objects.get(user=request.user)
    basket.subtotal -= product.price
    basket.products.remove(product)
    basket.save()
    return HttpResponseRedirect('/basket/')


def basket(request):
    categories = Category.objects.order_by("id")[0:5]
    if request.user.is_authenticated:
        products_in_basket = Product.objects.filter(
            basket=Basket.objects.get(user=request.user))
        basket = Basket.objects.get(user=request.user)
        if request.method == 'POST':
            new_order = Order.objects.create(user=request.user)
            for product in products_in_basket:
                new_order.products.add(product.id)
            new_order.total = basket.subtotal
            basket.subtotal = 0
            basket.products.set([])
            basket.save()
            new_order.save()
            return redirect(f'/orders/{new_order.id}')
        context = {'cats': categories, 'products_in_basket': products_in_basket,
                   'total_cost': basket.subtotal}
        return render(request, 'pages/basket.html', context=context)
    context = {'cats': categories}
    return render(request, 'pages/basket.html', context=context)


def order(request, pk):
    order_info = Order.objects.get(id=pk)
    order_products = Product.objects.filter(order=order_info)
    categories = Category.objects.order_by("id")[0:5]
    return render(request, 'pages/order.html', {'cats': categories, 'order': order_info, 'products': order_products})
