from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


def index(request: WSGIRequest):
    return render(request, 'main/main.html')


def user(request: WSGIRequest):
    #add here reading from DB
    return render(request, 'main/user.html')


def auth(request: WSGIRequest):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(f'Form is valid: {form.is_valid()}')
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'main/auth.html', context)