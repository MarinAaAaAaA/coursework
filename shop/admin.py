from django.contrib import admin
from .models import Product, Category, Seller, Rating, Callback, Order, Basket

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(Rating)
admin.site.register(Callback)
admin.site.register(Order)
admin.site.register(Basket)