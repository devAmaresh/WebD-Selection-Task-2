from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Post,Community,Friendship,Comment,Like,CommunityPost,Image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'profile_picture')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', 'post', 'like_or_dislike', 'created_at')


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    likes = LikeSerializer(many=True, read_only=True)
    is_friend = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('author', 'content', 'photo', 'created_at', 'likes', 'is_friend')

    def get_is_friend(self, obj):
        user = self.context['request'].user
        return obj.author in user.friendships_received.filter(status='accepted')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'


class CommunityPostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = CommunityPost
        fields = ('author', 'content', 'created_at', 'images')


class CommunitySerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    posts = CommunityPostSerializer(many=True, read_only=True)

    class Meta:
        model = Community
        fields = ('name', 'members', 'posts')

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

