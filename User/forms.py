from django import forms
from django.forms import widgets
from django.db.models import fields
from . models import Post, Users
from django.contrib.auth.forms import UsernameField,UserCreationForm,AuthenticationForm





class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':'True'}))
    password = forms.CharField(label="Password",strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}))

class DateInput(forms.DateInput):
    input_type = 'date'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user','text','created_at','updated_at']
        widgets = {
            'text' : forms.Textarea(attrs={'class':'form-control'}),
            'created_at' : DateInput(attrs={'class':'form-control'}),
            'updated_at' : DateInput(attrs={'class':'form-control'}),
        }