from django.shortcuts import render
from .models import *
# Create your views here.

def list_job(request):
    jobs = Job.objects.all()
    context ={
        'jobs':jobs
    }
    return render(request , 'pages/jobs.html' ,context)


def job_details(request , id):
    job = Job.objects.get(id = id)
    context ={
        'job':job
    }
    return render(request , 'pages/job_details.html' ,context)    