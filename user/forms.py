from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
import datetime

from .models import ProfileUser

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['password1'].required = True
        self.fields['password2'].required = True
        self.fields['password1'] = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Password")
        self.fields['password2'] = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Repeat password")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        widgets = {
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
        }

class LogInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['password'].required = True
        self.fields['username'] = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Email address")
        self.fields['password'] = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Password")
    
    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']

class SetupProfileForm(forms.ModelForm):
    phone_number = forms.RegexField(widget=forms.TextInput(
        attrs = {
            'type':'text',
            'class' : 'form-control'
        }
    ), regex=r'^\+?1?\d{9,15}$')
    def __init__(self, *args, **kwargs):
        super(SetupProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].error_messages = {'invalid_phone_number': 'Phone number must be entered in the format: \'+999999999\'. Up to 15 digits allowed.'}
        
    class Meta:
        model = ProfileUser
        fields = ['name', 'surname', 'middlename', 'birth_date', 'image', 'phone_number']
        my_validator = RegexValidator(r'^\+?1?\d{9,15}$')
        currentTime = datetime.datetime.now()
        currentYear = currentTime.year
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'middlename': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.SelectDateWidget(years=range(1900, currentYear+1), attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'})
        }