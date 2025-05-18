from django.urls import path
from . import views

urlpatterns = [
    path("signin", views.signIn, name='signIn'),
    path("signup", views.signUp, name='signUp'),
    path("signout", views.signOut, name='signOut'),
    path("profile", views.profile, name='profile')
]