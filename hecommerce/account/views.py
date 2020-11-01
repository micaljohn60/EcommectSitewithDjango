from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import CreateUserForm
from django.views.generic import View
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tonken import token_generator
from django.contrib import messages

# Create your views here.
def signup_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():              
            input_email = form.cleaned_data.get('email')
            user_mail = User.objects.filter(email=input_email)
            if user_mail.exists():
                messages.warning(request, "Email is already exist")
            else:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                # paht to view
                # get domain we are on
                # relative url to verfication
                # encode uid
                # token
                uidb64 =urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain 
                link =  reverse('account:activate',kwargs={
                    'uidb64':uidb64,'token':token_generator.make_token(user)})
                activate_url = 'http://'+domain+link
                email_subject = 'Activate your account'
                email_body = "Hi" + user.username + "Please Use this link to verify your account\n" + activate_url
                sent_to = form.cleaned_data.get('email')
                email = EmailMessage(
                    email_subject,
                    email_body,
                    settings.EMAIL_HOST_USER,
                    [sent_to]                
                )   
                
                email.send(fail_silently=False)
                form.save()
                return render(request,'acc_activate_email.html')
    
    return render(request,'signup.html',{'form':form})

class VerificationView(View):
    def get(self,request,uidb64,token):
        id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)
        
        if not token_generator.check_token(user,token):
            return redirect('account:log_in')
        if user.is_active:
            return redirect('account:log_in')
        user.is_active = True
        user.save()
        messages.success(request,'Account activated Successfully')
        return redirect('account:log_in')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)        
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                messages.warning(request,'Wrong User Name or password')
            else:
                login(request,user)
                return redirect('core:productlists')
    else:
        form = AuthenticationForm
    return render(request,'login.html',{'form':form})

def superuser_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:                
                login(request,user)
                return redirect('core:productlists')   
            else:
                 messages.warning(request,'Wrong User Name or password')
    else:
        form = AuthenticationForm
    return render(request,'sup-login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('core:productlists')
    
