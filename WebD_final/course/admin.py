from django.contrib import admin
from .models import Profile, Post, Community, Friendship, Comment, Like,CommunityPost,Image

@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at')

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
    list_display = ('community', 'author', 'content', 'created_at')


@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'status')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created_at')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'like_or_dislike', 'created_at')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
#customize the admin site header and title
admin.site.site_header = 'Social Media Admin'
