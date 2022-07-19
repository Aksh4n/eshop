from django.shortcuts import render , redirect
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth import authenticate , login , logout
from .forms import *
from text.models import *

def getvar(request):
	var = request.POST['option']
	print(var)
	return JsonResponse({
		'msg':'ok' , 'var':var
	}) 

def home(request):
	t = HomePageHeadLine.objects.get(id=1)

	return render(request, 'index.html', {'t':t})
def logout_user(request):
    logout(request)
    return redirect('home')

def shop(request):
	products = Product.objects.all()
	new = Product.objects.filter(category__name='new')
	data = cartData(request)
	star = Star.objects.all()
	cat = Category.objects.all()
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	sort_by = request.GET.get("sort", "l2h") 
	if sort_by == "l2h":
		products = Product.objects.all().order_by("price")
	elif sort_by == "h2l":
		products = Product.objects.all().order_by("-price")
	

	context = {'items':items, 'order':order, 'cartItems':cartItems ,'products':products , 'star':star, 'cat':cat, 'new':new}
	return render(request, 'shop.html', context )

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	if request.user.is_authenticated:
		customer = request.user.customer
	else:
		customer = None	

	form = OrderForm()
	form.fields['items'].initial = items 
	form.fields['complete'].initial = True
	form.fields['customer'].initial = customer
	form.fields['transaction_id'].initial = datetime.datetime.now().timestamp()


	

	context = {'items':items, 'order':order, 'cartItems':cartItems , 'form':form}
	if request.method == 'POST':

		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return JsonResponse({
				'msg':'success'
			})

		else:
			return JsonResponse({
				'msg':'err'
			})	
	return render(request, 'c2.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	option = data['option']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	if action == 'post':
		
		orderItem.option = option


	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse( {'msg': 'success'} , safe=False)
from django.db.models import Q
def searchProduct(request):
	if request.method == 'GET':
		data = cartData(request)
		star = Star.objects.all()
		cat = Category.objects.all()
		cartItems = data['cartItems']
		order = data['order']
		items = data['items']
		query= request.GET.get('q')
		if query is not None:
			lookups= Q(name__icontains=query) | Q(info__icontains=query)
			products= Product.objects.filter(lookups).distinct()
			context={'products': products,'items':items, 'order':order, 'cartItems':cartItems , 'star':star}
			print(products)		 
			return render(request, 'shop.html', context)
		else:
			return redirect('shop')
	else:
		return redirect('shop')

def searchProductByCat(request):
	if request.method == 'GET':
		data = cartData(request)
		star = Star.objects.all()
		cat = Category.objects.all()
		cartItems = data['cartItems']
		order = data['order']
		items = data['items']
		query= request.GET.get('q')
		if query is not None:
			lookups= Q(category__name=query)
			products= Product.objects.filter(lookups).distinct()
			context={'products': products,'items':items, 'order':order, 'cartItems':cartItems , 'star':star}
			print(products)		 
			return render(request, 'shop.html', context)
		else:
			return redirect('shop')
	else:
		return redirect('shop')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()  
            return JsonResponse({'msg': 'Success'})
    return render(request , 'contact.html', {})


def test(request):
	products = Product.objects.all()
	data = cartData(request)
	star = Star.objects.all()
	cat = Category.objects.all()
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	sort_by = request.GET.get("sort", "l2h") 
	if sort_by == "l2h":
		products = Product.objects.all().order_by("price")
	elif sort_by == "h2l":
		products = Product.objects.all().order_by("-price")
	

	context = {'items':items, 'order':order, 'cartItems':cartItems ,'products':products , 'star':star, 'cat':cat}


	return render(request, 'test.html', context)
from django.contrib.auth.forms import UserCreationForm
def register_user(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return JsonResponse({'msg':'Success'})
		else:
			return JsonResponse({'msg':'Err'})
def login_user(request):
	if request.method == "POST" :
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return JsonResponse({'msg':'Success'})
		else:
			return JsonResponse({'msg':'Err'})


def profile(request):
	return render(request, 'profile.html', {})
def about(request):
	return render(request, 'about.html', {})
def updateprofile(request):
	if request.method == "POST":
		customer = Customer.objects.get(id=request.user.customer.id)
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid:
			form.save()
			return JsonResponse({'msg':'Success'})
		else:
			return JsonResponse({'msg':'err'})


