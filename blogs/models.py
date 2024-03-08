from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "posts")

    name = models.CharField(max_length = 63)
    text = models.TextField()
    post_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    posted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Post {self.name} by {self.user.username} - {self.posted_at}"
    
    class Meta:
        ordering = ["posted_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"