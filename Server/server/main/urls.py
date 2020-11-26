from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('auth', views.auth),
    path('logout', views.logoutUser),
]
