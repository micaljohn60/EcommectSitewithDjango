from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import CreateUserForm

# Create your views here.
def signup_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():            
            form.save()
            return redirect('core:productlists')
    
    return render(request,'signup.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)        
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('core:productlists')
    else:
        form = AuthenticationForm
    return render(request,'login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('core:productlists')