from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, 'index.html')


def register(request):
    errors = User.objects.reg_validations(request.POST)
    print (errors)
    if len(errors) != 0:
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect ('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hash1,)
        request.session['name'] = user.first_name
        request.session['type'] = 'registered'
        print('user created')
        return redirect('/success/')

def login(request):
    errors = User.objects.login_validations(request.POST)
    if len(errors) > 0:
        for tag, error in errors.items():
            messages.error(request, error)
        print(errors)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['name'] = user.first_name
        request.session['type'] = 'logged in'
        request.session['id'] = user.id
        return redirect('/success/')

def success(request):
    return render(request,'success.html')
