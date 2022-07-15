from django.shortcuts import render , redirect
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth import authenticate , login , logout
from .forms import OrderForm
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
	options = Option.objects.all()
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	

	context = {'items':items, 'order':order, 'cartItems':cartItems ,'products':products , 'options':options }
	return render(request, 'shop.html', context)

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


       


    