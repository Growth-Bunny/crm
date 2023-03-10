from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.models import User
from . models import *



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))




class CustomerRegistrationForm(UserCreationForm):
    password1= forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email= forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    
    
    class Meta :
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent  
        fields = ['admin']

class LeadForm(forms.ModelForm):
   
    email= forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta :
        model = Leads
        fields = ['name', 'phone', 'email', 'destination', 'no_of_days', 'number_of_people' ,'city', 'assign']
        labels = {'email':'Email','destination':'Destination','no_of_days':"Number of Days",'city':'City of Travel'}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'phone':forms.NumberInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}),'destination':forms.TextInput(attrs={'class':'form-control'}),'no_of_days':forms.NumberInput(attrs={'class':'form-control'}),'number_of_people':forms.NumberInput(attrs={'class':'form-control'}),'city':forms.TextInput(attrs={'class':'form-control'}),'assign':forms.Select(attrs={'class':'form-control'})}

