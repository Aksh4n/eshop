from django import forms
from .models import  Order
import datetime

# Create your forms here.

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = ()
		feilds = '__all__'
	def __init__(self, *args, **kwargs):
		super(OrderForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['class']= 'form-control'
		self.fields['last_name'].widget.attrs['class']= 'form-control'
		self.fields['phone'].widget.attrs['class']= 'form-control'	
		self.fields['city'].widget.attrs['class']= 'form-select'
		self.fields['state'].widget.attrs['class']= 'form-select'
		self.fields['address'].widget.attrs['class']= 'form-control'	
		self.fields['postal_code'].widget.attrs['class']= 'form-control'
		self.fields['email'].widget.attrs['class']= 'form-control'
		self.fields['items'].widget.attrs['class']= 'form-control'	
		self.fields['complete'].widget.attrs['class']= ''
		self.fields['transaction_id'].widget.attrs['class']= 'form-control'
