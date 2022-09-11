from django import forms
from .models import Contact
from django.utils.translation import gettext as _


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'name',
            'number',
            'email',
            'subject',
            'messege',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': 'Ad Soyadınız',
                                    # 'id': 'value'
                                    
                                }),
            'number': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': 'Telefon nömrəniz',
                                    # 'id': 'value'
                                    
                                }),
            'email': forms.EmailInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': 'Email ünvanınız',
                                    # 'id': 'value1'
                                    
                                }),
            'subject': forms.TextInput(attrs={
                                    'class': 'form-group ',
                                    'placeholder': 'Mövzu',
                                    # 'id': 'value2'
                                }),
            'messege': forms.Textarea(attrs={
                                    'class': 'form-group ',
                                    'placeholder': 'Mesajınız',
                                    'cols': "30", 
                                    'rows': "10"
                                    # 'id': 'value3'
                                })
        }
