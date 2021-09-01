from django.urls import path
from .views import UserCreateView, home 

urlpatterns = [
    path('',home, name='home'),
    path('user',UserCreateView.as_view(), name='user'),
]