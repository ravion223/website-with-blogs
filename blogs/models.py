from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)

    name = models.CharField(max_length=200, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True, upload_to="profile/")
    email = models.EmailField(blank=True, null=True)
    date_of_creation = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"
    
    class Meta:
        ordering = ["date_of_creation"]
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "posts")
    likes = models.ManyToManyField(User, related_name='liked_posts')

    title = models.CharField(max_length = 63)
    text = models.TextField()
    post_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    posted_at = models.DateTimeField(auto_now_add = True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return f"Post '{self.title}' by {self.author.username} - {self.posted_at}"
    
    class Meta:
        ordering = ["posted_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Commentary(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "commentaries")
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "commentaries")

    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f"Commentary by {self.author.username} on post {self.post} - {self.posted_at}"
    
    class Meta:
        ordering = ["posted_at"]
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"