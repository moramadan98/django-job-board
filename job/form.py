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
        
        # labels ={
        #     'name':'',
        #     'email':'',
        #     'link':'',
        #     'cv':'',
        #     'coverletter':'',
        # }



class Jobform(forms.ModelForm):
   
    class Meta:
        model= Job
        fields = ['title','jobtype','vacancy','experience','salary','job_img','description','benefits','qualification','categoty' ]
        widgets ={
            'title': forms.TextInput(attrs={'placeholder':'Job title'}),
            'jobtype': forms.Select(attrs={ 'class':'wide'} ),
            'vacancy': forms.NumberInput(attrs={'placeholder':'vacancy'}),
            'experience':forms.NumberInput(attrs={'placeholder':'experience'}),
            'salary':forms.NumberInput(attrs={'placeholder':'salary'}),
            'categoty': forms.Select(attrs={'class':'wide'}),
            'job_img': forms.FileInput(attrs={'class':'custom-file-input'}),
            'description': forms.Textarea(attrs={'placeholder':'Description'}),
            'benefits': forms.Textarea(attrs={'placeholder':'Benefits'}),
            'qualification': forms.Textarea(attrs={'placeholder':'Qualification'}),
        }

        