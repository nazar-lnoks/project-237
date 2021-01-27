from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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