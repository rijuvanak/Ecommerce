from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
import Eapp.models
# Create your views here.
from .decorators import auth_user
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login

from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Product


def login_index1(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        password = request.POST.get('password')

        check_user = cdb.objects.filter(cname=cname, password=password)
        if check_user:
            request.session['users'] = cname
            return redirect('dashboard')
        else:
            return HttpResponse('Please enter valid Username or Password.')
    return render(request, 'login_index1.html')


@auth_user
def dashboard(request):
    return render(request, 'dashboard.html')



@auth_user
def users(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        email = request.POST['email']
        password = request.POST.get('password')
        confirm_password = request.POST['confirm_password']
        # print(uname, pwd)
        if cdb.objects.filter(cname=cname).count() > 0:
            return HttpResponse('Username already exists.')
        else:
            users = cdb(cname=cname, email=email, password=password, confirm_password=confirm_password)
            users.save()
            return redirect('login_index1')
    else:
        return render(request, 'users.html')



@auth_user
def dashboardmain(request):
    products = Product.objects.all()
    return render(request, 'dashboardmain.html', {'products': products})





from django.shortcuts import render, get_object_or_404
import Eapp.models



@auth_user
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)  # Get the product object

    cart_item, created = CartItem.objects.get_or_create(product=product)
    # Get or create the cart item associated with the user and the product

    if not created:
        cart_item.quantity += 1  # Increment the quantity if the cart item already exists
        cart_item.save()

    return redirect('cart')  # Redirect to the cart page




@auth_user
def cart(request):
    cart_items = CartItem.objects.all()  # Retrieve all cart items

    total_quantity = 0  # Initialize total quantity
    total_amount = 0  # Initialize total amount

    for cart_item in cart_items:
        total_quantity += cart_item.quantity  # Calculate total quantity
        total_amount += cart_item.product.price * cart_item.quantity  # Calculate total amount for each cart item

    context = {
        'cart_items': cart_items,
        'total_quantity': total_quantity,
        'total_amount': total_amount
    }

    return render(request, 'cart.html', context)

@auth_user
def logout(request):
    try:
        del request.session['users']
    except:
        return redirect('login_index1')
    return redirect('login_index1')



@auth_user
def cartlist(request):
    cart_items = CartItem.objects.all()
    return render(request, 'cartlist.html', {'cart_items': cart_items})


from django.shortcuts import render, redirect
from .models import CartItem


@auth_user
def edit_item(request,CartItem_id):
    cart_item = CartItem.objects.get(id=CartItem_id)

    if request.method == 'POST':
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')

        cart_item.product.name = product
        cart_item.quantity = quantity
        cart_item.save()
        return redirect('cartlist')

    return render(request, 'edit_item.html', {'cart_item': cart_item})


@auth_user
def delete_item(request, CartItem_id):
    cart_item = CartItem.objects.get(id=CartItem_id)

    if request.method == 'POST':
        cart_item.delete()
        return redirect('cartlist')

    return render(request, 'delete_item.html', {'cart_item': cart_item})
