from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

COMMENT_SIZE = 1024

class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].required = True
        self.fields['rate'].required = True
        self.fields['comment'] = forms.CharField(max_length=COMMENT_SIZE, widget=forms.Textarea(attrs={'rows': 3, 'cols': 40, 'style':'resize:none;'}), label='Your comment')
    class Meta:
        model = models.Feedback
        fields = ['comment', 'rate']
        widgets = {
            'rate': forms.NumberInput(attrs={'step': 0.1} ),
        }
        
class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deliveryAddress'].required = True
        self.fields['payment'].required = True
        self.fields['deliveryAddress'] = forms.CharField(widget=forms.TextInput(), label='Delivery address')
        self.fields['payment'] = forms.CharField(widget=forms.RadioSelect(choices=(('Test1', 'Value1'), ('Test2', 'Value2'))), label='Payment method')
    class Meta:
        model = models.Order
        fields = ['deliveryAddress', 'payment']