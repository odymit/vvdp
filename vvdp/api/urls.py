from django.urls import path

from . import views

urlpatterns = [
    path('user/login', views.userlogin, name='login'),
    path('search', views.search, name='search'),
]
