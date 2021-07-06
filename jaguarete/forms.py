
from django import forms

from .models import Product
  
class ProductForm(forms.ModelForm):
    long_description = forms.CharField(widget=forms.Textarea(
        attrs={
        'class':'form-control',
        'placeholder':'Descripcion larga',
        'style': 'height: 100%'
        }
    ))
    brief_description = forms.CharField(widget=forms.Textarea(
        attrs={
        'class':'form-control',
        'placeholder':'Descripcion Corta',
        'style': 'height: 100%'
        }
    ))
    title = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        }
    ))
    price = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
        }
    ))
    class Meta:
        model = Product
        fields = '__all__'
