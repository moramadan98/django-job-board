from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_job, name ='jobs'),
    path('<int:id>',views.job_details, name ='job_details'),
]