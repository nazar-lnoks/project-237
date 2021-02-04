from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

COMMENT_SIZE = 1024
ROWS = 3
COLUMNS = 40

class FeedbackForm(forms.ModelForm):
    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['comment'].required = True
        self.fields['comment'] = forms.CharField(max_length=COMMENT_SIZE, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': ROWS, 'cols': COLUMNS, 'style':'resize:none'}), label='Your comment')
    class Meta:
        model = models.Feedback
        fields = ['comment']

        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': ROWS, 'cols': COLUMNS})
        }
        
class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deliveryAddress'].required = True
        self.fields['payment'].required = True
        # self.fields['deliveryAddress'] = forms.CharField(widget=forms.TextInput(), label='Delivery address')
        self.fields['payment'] = forms.CharField(widget=forms.RadioSelect(choices=(('cash', 'Cash'),)), label='Payment method')

    class Meta:
        model = models.Order
        fields = ['deliveryAddress', 'payment']

        widgets = {
            'deliveryAddress': forms.TextInput(attrs={'class': 'form-control'})
        }