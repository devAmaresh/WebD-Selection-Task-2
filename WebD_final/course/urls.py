from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', user_registration_view, name='register'),
    path('profile/', user_profile_view, name='profile'),
    path('posts/', post_list_view, name='post-list'),
    path('communities/', community_list_view, name='community-list'),
    path('friend-request/<int:to_user_id>/', send_friend_request, name='send-friend-request'),
    path('accept-friend-request/<int:from_user_id>/', accept_friend_request, name='accept-friend-request'),
    path('post-comments/<int:post_id>/', post_comments_view, name='post-comments'),
    path('posts/<int:post_id>/like/', like_post, name='like-post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
