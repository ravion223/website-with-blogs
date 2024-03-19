from django.shortcuts import render, redirect
from .models import Post, Commentary, Profile
from django.http import HttpResponseRedirect
from .forms import PostForm, EditProfileForm
from django.shortcuts import get_object_or_404

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


def get_profile(request):
    profile = Profile.objects.get(user=request.user)

    context = {
        'profile': profile,
    }

    return render(
        request,
        'blogs/profile.html',
        context
    )


def post_form(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()

    return render(request, 'blogs/post-form.html', {'form': form})


def edit_profile_view(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')
    else:
        form = EditProfileForm(instance=request.user.profile)

    return render(
        request,
        'blogs/edit-profile-form.html',
        {'form': form}
    )