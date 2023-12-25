from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            print("logged in")
            return render(request,'home.html')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        email = request.POST.get('email')
        username = email.split('@')[0]

        if password != repassword:
            return render(request, 'registration/register.html', {'error_message': 'Passwords do not match.'})
        elif User.objects.filter(username=username).exists():
            return render(request, 'registration/register.html', {'error_message': 'Username already exists.'})
        else:
            user = User.objects.create_user(username = username, email = email, password = password)
            user.save()
            return render(request, 'registration/login.html', {})
    return render(request, 'registration/register.html', {})

def change_password(request):
    return render(request, 'home.html', {})