from django.shortcuts import render ,redirect
from .forms import Signupform
from django.contrib.auth import authenticate,login
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.changed_data[0]
            password = form.changed_data[1]
            user = authenticate(username = username , password = password)
            login(request ,user)
            return redirect('/accounts/profile')
    else:
        form = Signupform()    
    return render(request ,'registration/signup.html',{'form':form})