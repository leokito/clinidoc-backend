from django.contrib import admin
from django.urls import path
from account.views import UserCreationView, UserLogin, UserView

urlpatterns = [
    path('signup/', UserCreationView.as_view()),
    path('signin/', UserLogin.as_view()),
    path('user/', UserView.as_view())
]
