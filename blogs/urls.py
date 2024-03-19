from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_posts, name="posts-list"),
    path('post/<int:pk>', get_post, name="post-detail"),
    path('post-form/', post_form, name="post-form"),
    path('profile/', get_profile, name="profile"),
    path('edit-profile-form/', edit_profile_view, name="edit-profile-form")
]