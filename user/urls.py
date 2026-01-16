from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signin/", views.signIn, name='signIn'),
    path("signup/", views.signUp, name='signUp'),
    path("signout/", views.signOut, name='signOut'),
    path("profile/", views.profile, name='profile')
]
