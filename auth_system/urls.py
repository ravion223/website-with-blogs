from django.urls import path
from .views import register_view, login_view, logout_view, EditProfileView, PasswordsChangeView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register_view, name='registration-form'),
    path('login/', login_view, name="login-form"),
    path('logout/', logout_view, name="logout"),
    path('edit-profile/', EditProfileView.as_view(), name='update-form'),
    path('password/', PasswordsChangeView.as_view(template_name='auth_system/change-password-form.html'), name='change-password'),
]