from django.urls import path
from .views import profile, user_login, user_register
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", user_login),
    path("logout/", LogoutView.as_view(),
         {'next_page': settings.LOGOUT_REDIRECT_URL}),
    path("register/", user_register),
    path('profile/', profile)
]
