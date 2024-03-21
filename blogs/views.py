from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Commentary, Profile
from django.http import HttpResponseRedirect
from .forms import PostForm, EditProfileForm, CommentaryForm
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.

from django.shortcuts import render
from .models import Post, Profile

def get_all_posts(request):
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            pass

    posts = Post.objects.all()

    context = {
        "posts": posts,
        "profile": profile
    }

    return render(
        request,
        "blogs/posts-list.html",
        context
    )


# def get_all_posts(request):
#     posts = Post.objects.all()
#     profile = Profile.objects.get(user=request.user)

#     context = {
#         "posts": posts,
#         "profile": profile
#     }

#     return render(
#         request,
#         "blogs/posts-list.html",
#         context
#     )


def get_post(request, pk: int):
    post = Post.objects.get(id=pk)
    form = CommentaryForm()
    stuff = get_object_or_404(Post, id=pk)
    total_likes = stuff.total_likes()
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            pass

    liked = False
    if stuff.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if form.is_valid:
            commentary = form.save(commit=False)
            commentary.post = post
            commentary.author = request.user
            commentary.save()
            return redirect('post-detail', pk=post.id)

    context = {
        "post": post,
        "commentaries": post.commentaries.all(),
        "form": form,
        'total_likes': total_likes,
        'liked': liked,
        'profile': profile,
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
        'posts': profile.user.posts.all()
    }

    return render(
        request,
        'blogs/profile.html',
        context
    )


def get_profile_by_id(request, pk):
    sprofile = get_object_or_404(Profile, id=pk)
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            pass

    context = {
        'sprofile': sprofile,
        'profile': profile,
        'posts': sprofile.user.posts.all()
    }

    return render(
        request,
        'blogs/sprofile.html',
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
        profile = None
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
            except Profile.DoesNotExist:
                pass

    return render(request, 'blogs/post-form.html', {'form': form, 'profile': profile})


def edit_profile_view(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')
    else:
        form = EditProfileForm(instance=request.user.profile)
        profile = Profile.objects.get(user=request.user)

    return render(
        request,
        'blogs/edit-profile-form.html',
        {'form': form, 'profile': profile}
    )


def search_blogs(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)
        profile = None
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
            except Profile.DoesNotExist:
                pass
        return render(
            request,
            'blogs/search-blogs.html',
            {'searched': searched, 'posts': posts, 'profile': profile}
        )
    else:
        return render(
        request,
        'blogs/search-blogs.html',
    )


def like_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))