from django.contrib import admin
from django.urls import path, include
from shop.views import index, product, products, category, seller, callback, basket, order, addToBasket, removeItemFromBasket, \
    categories
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('user.urls')),
    path('', index),
    path('products/', products),
    path('products/<int:pk>', product),
    path('category/<int:pk>', category),
    path('sellers/<int:pk>', seller),
    path('basket/', basket),
    path('leave-callback/', callback),
    path('orders/<int:pk>', order),
    path('basket/add/<int:pk>', addToBasket),
    path('basket/remove-item/<int:pk>', removeItemFromBasket),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)