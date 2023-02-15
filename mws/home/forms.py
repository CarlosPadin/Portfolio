from django import forms
from django.forms import TextInput, EmailInput, Textarea
from . import models

class createMessage(forms.ModelForm):
    class Meta:
        model = models.Messages
        fields = ['UserName', 'Email', 'Message']
        widgets = {
            'UserName': TextInput(attrs={
                'class': "form-control bg-white text-dark",
                'placeholder': "Name"    
            }),
            'Email': EmailInput(attrs={
                'class': "form-control bg-white text-dark",
                'placeholder': "Email"    
            }),
            'Message': Textarea(attrs={
                'class': "form-control bg-white text-dark",
                'placeholder': "Message",
                'rows': '5'    
            })
        }
