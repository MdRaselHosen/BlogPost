from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-data_posted')
    context = {
        'posts': posts
    }
    return render(request, 'home.html',context)


def blog_details(request,pk):
    blog = Post.objects.get(pk=pk)
    print("blog is ", blog)
    context = {
        'blog':blog
    }
    return render(request, "blog_detail.html",context)