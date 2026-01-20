from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages
from base.models import Post
from .forms import ProfileUpdateForm, UserUpdateForm

# Create your views here.



def signIn(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.error(request, "Invalid Username")
            return redirect(request.path)
        
    return render(request, 'signin.html')


def signUp(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('conf_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username Already exists")
            return redirect(request.path)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already exist")
            return redirect(request.path)
        
        print(password1,password2)
        if password1 != password2:
            messages.error(request, "passwords not matched.")
            return redirect(request.path)

        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            return redirect('signIn')
        except:
            messages.error(request, "Something went wrong")
            return redirect(request.path)
    return render(request, 'signUp.html')


def signOut(request):
    logout(request)
    storage = get_messages(request)
    for _ in storage:
        pass
    

        
    return render(request, 'signOut.html')


@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    user = request.user
    blogs = Post.objects.filter(author=request.user)
    context = {
        'user':user,
        'blogs':blogs,
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'profile.html',context)