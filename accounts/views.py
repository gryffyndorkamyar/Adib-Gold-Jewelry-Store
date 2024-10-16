from django.shortcuts import redirect, render 
from .forms import CustomUserCreationForm , CustomLoginForm
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages
from django.core.mail import send_mail
from Adib import settings
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            msg = f" در سایت ثبت نام کرد {user.username} کاربر با نام کاربری  "
            send_mail("ثبت نام کاربر",
                      msg,
                      settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER]) 
            
            return redirect("signup_success")
        
    else:
        form = CustomUserCreationForm()
    
    return render(request,"accounts/signup.html",{'form':form})

def signup_success(request):
    return render(request,"accounts/register_success.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect("shop:home")
                
                else:
                    messages.error(request, 'حساب کاربری شما غیرفعال است.')

            else:
               messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
    else:
        form = CustomLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("shop:home")