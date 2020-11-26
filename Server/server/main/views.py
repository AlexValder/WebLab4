from django.shortcuts import redirect, render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth')
def index(request: WSGIRequest):
    return render(request, 'main/main.html')


def user(request: WSGIRequest):
    #add here reading from DB
    return render(request, 'main/user.html')


def auth(request: WSGIRequest):
    form = CreateUserForm()
    context = dict()
    print(request.POST)
    if request.method == 'POST':
        if 'email' in request.POST:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data.get('username')
                form.save()
                return render(request, 'main/auth_success.html', {'username':user, 'up_or_in': 'Signed UP'})
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'main/main.html')
            context['signinerror'] = 'Wrong password or email.'
    context['form'] = form
    return render(request, 'main/auth.html', context)


def logoutUser(request: WSGIRequest):
    logout(request)
    return redirect('/auth')