from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_posts, name="posts-list"),
    path('post/<int:pk>', get_post, name="post-detail"),
]