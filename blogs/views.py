from django.shortcuts import render, redirect
from .models import Post, Commentary

# Create your views here.

def get_all_posts(request):
    posts = Post.objects.all()

    context = {
        "posts": posts
    }

    return render(
        request,
        "blogs/posts-list.html",
        context
    )


def get_post(request, pk: int):
    post = Post.objects.get(id=pk)

    context = {
        "post": post
    }

    return render(
        request,
        "blogs/post-detail.html",
        context
    )