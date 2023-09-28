from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from userauths.forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, Registered Successfully.")
            
            new_user = authenticate(username=new_user.email, password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("userauths:sign-in")
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'userauths/sign-up.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("storeroom:index")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "you are logged in.")
                return redirect("storeroom:index")
            
        else:
            messages.warning(request, 'user does not Exit. create an account')
    else:
        form = LoginForm()
    context = {
        "form":form
    }
    return render(request, 'userauths/sign-in.html', context)




def user_logout(request):
    logout(request)
    messages.success(request, "you logged out.")
    return render(request, "userauths/sign-out.html")