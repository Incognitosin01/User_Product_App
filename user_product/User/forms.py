from django.forms import ModelForm, widgets
from django import forms
from .models import Post
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('user','text')

        widgets = {
            'user' : forms.Select(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control'})
        }
