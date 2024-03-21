from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from .forms import EditProfileForm
from blogs.models import Profile


# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
        profile = None
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
            except Profile.DoesNotExist:
                pass

    return render(request,
                'auth_system/registration-form.html',
                {'form': form, 'profile': profile}
    )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                messages.error(request, "Wrong username or password")

            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
        profile = None
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
            except Profile.DoesNotExist:
                pass

    return render(
        request,
        "auth_system/login-form.html",
        {"form": form, 'profile': profile}
    )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class EditProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'auth_system/user-edit-profile-form.html'
    success_url = '/'

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = '/'