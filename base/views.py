from django.shortcuts import render, redirect, get_object_or_404
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

@login_required
def update(request, pk):
    post =get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('content')
        post.title = title
        post.content = body
        post.save()

        return redirect('blog_detail', pk=post.pk)
    
    return render(request, "update.html", {'post':post})

@login_required
def delete(request, pk):
    delete_post = Post.objects.get(pk=pk)
    delete_post.delete()
    return redirect('home')