from django.shortcuts import redirect, render
from accounts.forms import RegisterForm
# Create your views here.

def home(request):
    return render(request,'home.html')


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form': form})


def dashboard(request):
    return render(request,'dashboard.html')


# built-in LoginView searches for -> registration/login.html