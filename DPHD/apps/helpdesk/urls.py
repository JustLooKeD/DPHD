from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='signin'),
    path('create', views.create, name='create'),
    path('adm', views.adm, name='adm')
]