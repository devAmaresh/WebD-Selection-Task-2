from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Profile, Post,Community,Friendship,Comment,Like
from .serializers import UserSerializer, ProfileSerializer, PostSerializer,CommentSerializer,CommunitySerializer,LikeSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

@api_view(['POST'])
def user_registration_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile_view(request):
    profile = request.user.profile
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list_view(request):
    user = request.user  # Get the authenticated user
    
    if request.method == 'GET':
        friends = user.friendships_received.filter(status='accepted').values_list('from_user', flat=True)
        posts = Post.objects.filter(author__in=friends) | Post.objects.filter(author=user)
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=user)  # Use the authenticated user as the author
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def community_list_view(request):
    if request.method == 'GET':
        communities = Community.objects.all()
        serializer = CommunitySerializer(communities, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_friend_request(request, to_user_id):
    from_user = request.user
    to_user = User.objects.get(id=to_user_id)
    friendship, created = Friendship.objects.get_or_create(from_user=from_user, to_user=to_user)
    return Response({'message': 'Friend request sent'}, status=201)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_friend_request(request, from_user_id):
    to_user = request.user
    from_user = User.objects.get(id=from_user_id)
    friendship = Friendship.objects.get(from_user=from_user, to_user=to_user)
    friendship.status = 'accepted'
    friendship.save()
    return Response({'message': 'Friend request accepted'}, status=200)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_comments_view(request, post_id):
    if request.method == 'GET':
        comments = Comment.objects.filter(post_id=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post_id=post_id)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response({'message': 'Post not found'}, status=404)
    
    user = request.user
    like_or_dislike = request.data.get('like_or_dislike')  # True for like, False for dislike
    
    if like_or_dislike is None:
        return Response({'message': 'Please provide like_or_dislike parameter'}, status=400)
    
    like, created = Like.objects.get_or_create(user=user, post=post)
    like.like_or_dislike = like_or_dislike
    like.save()
    
    return Response({'message': 'Like updated successfully'}, status=200)



