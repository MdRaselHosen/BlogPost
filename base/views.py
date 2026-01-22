from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    posts_list = Post.objects.all().order_by('-data_posted')
    # code for pagination
    paginator = Paginator(posts_list, 4)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

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


@login_required
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        Post.objects.create(
            title = title,
            content = body,
            author = request.user         
        )
        return redirect("home")


    return render(request, "create_blog.html")