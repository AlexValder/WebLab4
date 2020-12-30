from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'^anime/(\S+)$', views.anime),
    path('user', views.user),
    path('auth', views.auth),
    path('logout', views.logoutUser),
    path('favicon.ico', RedirectView.as_view(url='/static/main/res/favicon.ico'), name='favicon'),
]
