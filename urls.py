from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.demo,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('live',views.live,name='live'),
    path('shopping', views.shopping, name='shopping'),
    path('service', views.service, name='service'),
    path('cart/', views.cart, name='cart'),
    path('addcart/<int:id>/', views.addcart, name='addcart'),
    path('de_cart/<int:id>/', views.de_cart, name='de_cart'),
    path('plusqty/<int:id>/',views.plusqty,name='plusqty'),
    path('minusqty/<int:id>/',views.minusqty,name='minusqty'),
    path('checkout', views.checkout, name='checkout'),
    path('logout', views.logout, name='logout'),
####reset password urls####
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/login/',views.login,name='login'),
]