
from django import forms
  
# import GeeksModel from models.py
from .models import Product
  
class ProductForm(forms.ModelForm):
     class Meta:
         model = Product
         fields = '__all__'

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)