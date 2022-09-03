from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, AccountAuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def account_login(request):
    user = request.user
    if user.is_authenticated:
        return redirect('account-profile')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            acc = authenticate(username=username, password=password)
            if acc:
                login(request, acc)
                return redirect('account-profile')
    else:
        form = AccountAuthenticationForm()
    return render(request, 'account/login.html', {'form':form})
            



def account_register(request):
    if(request.method == 'POST'):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            username = data.get('username')
            raw_pass = data.get('password1')
            account = authenticate(username=username, password=raw_pass)
            login(request, account)
            return redirect('account-login')
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form':form})

def account_logout(request):
    logout(request)
    return redirect('account-login')
    


def account_profile(request):
    return render(request, 'account/profile.html')