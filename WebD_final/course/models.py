from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    photo = models.ImageField(upload_to='post_photos/', blank=True, null=True)  # Add this line for photos
    created_at = models.DateTimeField(auto_now_add=True)

class Community(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('auth.User', related_name='communities')


class CommunityPost(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField('Image', related_name='community_posts', blank=True)


class Image(models.Model):
    image = models.ImageField(upload_to='community_images/')

class Friendship(models.Model):
    from_user = models.ForeignKey('auth.User', related_name='friendships_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey('auth.User', related_name='friendships_received', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted')], default='pending')

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_or_dislike = models.BooleanField(default=True)  # True for like, False for dislike
    created_at = models.DateTimeField(auto_now_add=True)
