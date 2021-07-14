from django.forms import ModelForm, widgets
from django import forms
from .models import Product
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name' : forms.Textarea(attrs={'class':'form-control'}),
            'weight' : forms.NumberInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class' : 'form-control'})
        }
