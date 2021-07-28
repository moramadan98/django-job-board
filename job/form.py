from django import forms
from .models import *


class Applyform(forms.ModelForm):
    
    class Meta:
        model = Apply_job
        fields = ['name','email','link','cv','coverletter']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email'}),
            'link': forms.URLInput(attrs={'placeholder':'Website/Portfolio link'}),
            'cv': forms.FileInput(attrs={'class':'custom-file-input'}),
            'coverletter': forms.Textarea(attrs={'placeholder':'Coverletter'}),
        }
        
        labels ={
            'name':'',
            'email':'',
            'link':'',
            'cv':'',
            'coverletter':'',
        }

    