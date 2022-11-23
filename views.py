from django.shortcuts import render
from django.shortcuts import redirect
from dairyapp.forms import CustomUserCreationForm
from django.urls import reverse
from django.http import HttpResponse, request
from . models import *
from django.contrib import auth,messages
from django.contrib.auth.models import User
from hashlib import sha256
from .models import Products,Services
from dairyapp.models import Cart
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.
from django.shortcuts import render,redirect
def demo(request):
    return render(request,"home.html")

def live(request):
    return render(request,"live.html")

def checkout(request):
    return render(request,"checkout.html")

@login_required(login_url='login')
def cart(request):
    user = request.user
    cart=Cart.objects.filter(user_id=user)
    total=0
    for i in cart:
        total += i.product.price * i.product_qty
    category=Category.objects.all()
    return render(request,'Cart.html',{'cart':cart,'total':total,'category':category})

# Add to Cart.
@login_required(login_url='login')
def addcart(request, id):
    user = request.user
    item = Products.objects.get(id=id)
    if item.stock > 0:
        if Cart.objects.filter(user_id=user, product_id=item).exists():
            return redirect(cart)
        else:
            product_qty = 1
            price = item.prd_price * product_qty
            new_cart = Cart(user_id=user.id, product_id=item.id, product_qty=product_qty, price=price)
            new_cart.save()
            return redirect(cart)


#Cart Quentity Plus Settings
def plusqty(request, id):
    cart = Cart.objects.filter(id=id)
    for cart in cart:
        if cart.product.stock > cart.product_qty:
            cart.product_qty += 1
            cart.price = cart.product_qty * cart.product.price
            cart.save()
            return redirect('cart')
        # messages.success(request, 'Out of Stock')
        return redirect('cart')


# Cart Quentity Plus Settings
def minusqty(request, id):
    cart = Cart.objects.filter(id=id)
    for cart in cart:
        if cart.product_qty > 1:
            cart.product_qty -= 1
            cart.price = cart.product_qty * cart.product.price
            cart.save()
            return redirect('cart')
        return redirect('cart')


# View Cart Page
@login_required(login_url='login')
def cart(request):
    user = request.user
    cart = Cart.objects.filter(user_id=user)
    total = 0
    for i in cart:
        total += i.product.prd_price * i.product_qty

    # subcategory = Subcategory.objects.all()
    return render(request, 'Cart.html',
                  {'cart': cart, 'total': total})


# Remove Items From Cart
def de_cart(request, id):
    Cart.objects.get(id=id).delete()
    return redirect(cart)

# def registration(request):
#     if request.method=='POST':
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         username = request.POST['username']
#         email=request.POST['email']
#         pwd1=request.POST['pwd1']
#         pwd2=request.POST['pwd2']
#
#
#         if pwd1==pwd2:
#             if register.objects.filter(email=email).exists():
#                 print("exists")
#                 return redirect('shopping')
#             else:
#                 register(first_name=first_name, last_name=last_name, username=username, email=email, pwd1=pwd1, pwd2=pwd2).save()
#                 login(email=email,pwd1=pwd1).save()
#                 print("reg")
#                 # return redirect('company/')
#                 return redirect('shopping')
#
#         else:
#             print("not match")
#             return redirect('login')
#     else:
#         return render(request,'register.html')
#
#
#
#
#
def shopping(request):
    dict_shp={
        'product':Products.objects.all()
    }


    return render(request,"shopping.html",dict_shp)
def service(request):
    services = Services.objects.all()

    return render(request,"service.html",{'service':services})

#
#
# def userlogin(request):
#     request.session.flush()
#     if 'email' in request.session:
#         return redirect('shopping')
#     if request.method=='POST':
#         email=request.POST['email']
#         pwd1=request.POST['pwd1']
#         print(email,pwd1)
#                # password2=sha256(pwd1.encode()).hexdigest()
#                # print(password2)
#         new_user=register.objects.filter(email=email,pwd1=pwd1)
#         print(new_user)
#         if new_user:
#             print('1')
#             user_details=register.objects.get(email=email)
#             print('2')
#             email=user_details.email
#             request.session['email'] = email
#             return redirect('shopping')
#     else:
#         print("invalid")
#         return render(request,"login.html")
#
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password)
                user.save();
                print("user Created")
                messages.success(request, "Account Created Successfully")
        else:
            print("password not match")
            messages.info(request, "Password incorrect")
            return redirect('register')
        return redirect('login')
    return render(request, "register.html")

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('live')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")





def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')
 # ........   services.........
