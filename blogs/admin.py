from django.contrib import admin
from .models import Post, Commentary, Profile

# Register your models here.

admin.site.register(Post)
admin.site.register(Commentary)
admin.site.register(Profile)