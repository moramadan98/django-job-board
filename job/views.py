from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from .form import *
from django.core.exceptions import ValidationError
from django.contrib import messages
# Create your views here.

def list_job(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 6) # Show 6 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={
        'jobs':page_obj
    }
    return render(request , 'pages/jobs.html' ,context)


def job_details(request , slug):
    job = Job.objects.get(slug = slug)
    if request.method == 'POST':
        data = Applyform(request.POST , request.FILES)
        if data.is_valid():
            mydata = data.save(commit= False)
            mydata.job=job
            mydata.save()
            messages.success(request, 'Apply successfully.')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request , 'Invalid input')    
    context ={
        'job':job,
        'form':Applyform
    }
    return render(request , 'pages/job_details.html' ,context)    