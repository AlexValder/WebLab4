from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from .models import Comments


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class AddCommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment', 'usrname', 'date', 'slugTitle']