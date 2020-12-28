from django.db import models
from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, AddCommentForm
from .models import Anime, Comments
from datetime import  datetime


@login_required(login_url='/auth')
def index(request: WSGIRequest):
    animes = Anime.objects.all()
    return render(request, 'main/main.html', {'animes': animes})


def user(request: WSGIRequest):
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
                return redirect('/')
                #return render(request, 'main/main.html')
            context['signinerror'] = 'Wrong password or email.'
    context['form'] = form
    return render(request, 'main/auth.html', context)


@login_required(login_url='/auth')
def anime(request: WSGIRequest, slugname):
    slugname = slugname.replace('"', '')
    if request.method == 'POST':
        comment = request.POST.get('comment')
        request.POST._mutable = True
        request.POST.appendlist('usrname', request.user.username)
        request.POST.appendlist('date', datetime.today())
        request.POST.appendlist('slugTitle', slugname)
        request.POST._mutable = False
        form = AddCommentForm(request.POST)
        print(f'CLEANED DATA: {form.fields}')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
        else:
           print('Some error happend: form is not valie\n{}'.format(form))
    anime = Anime.objects.filter(slugTitle=slugname)
    comments = Comments.objects.filter(slugTitle=slugname)
    if anime:
        return render(request, 'main/anime.html', {'title': anime[0].title, 'description': anime[0].description, 'genre': anime[0].genre, 'picture': anime[0].picture, 'released': anime[0].released, 'comments': comments})
    return HttpResponse('Error 404: page not found.')


def logoutUser(request: WSGIRequest):
    logout(request)
    return redirect('/auth')