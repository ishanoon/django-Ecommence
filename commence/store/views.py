from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def store(request):
    products = Product.objects.all()
    context = {"products": products}
    return  render(request, "store/store.htm", context)

@login_required(login_url="login")
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total" : 0, "get_cart_items": 0}
    context = {"items" : items, "order" : order }
    return  render(request, "store/cart.htm", context)

@login_required(login_url="login")
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total" : 0, "get_cart_items": 0}
    context = {"items" : items, "order" : order }
    return  render(request, "store/checkout.htm", context)

def UserCreation(request):
    if request.user.is_authenticated:
        return redirect("store")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account succesfully created for " + user)
                    
                return redirect("login")
    
    context = {'form':form}
    return render(request,"store/register.htm",context)

def UserLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("store")
        else:
            messages.info(request, "Username Or password incorrect")
    
    context = {}
    return render(request, "store/login.htm", context)

def viewStore(request, pk):
    products = Product.objects.get(id = pk)
    
    context= {"products": products}

    return render(request,"store/view.htm",context)

def logoutUser(request):
    logout(request)
    return redirect("login")

def UserPage(request):
    return render(request, "store/user.htm")