from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_job, name ='jobs'),
    path('<str:slug>',views.job_details, name ='job_details'),
]