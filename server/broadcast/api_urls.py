from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import BroadcastMessageViewSet, get_user_broadcast

router = DefaultRouter()
router.register(r'messages', BroadcastMessageViewSet, basename='broadcastmessage')

urlpatterns = [
    path('', include(router.urls)),
    # PUBLIC broadcast endpoint - no authentication required
    path('<slug:user_slug>/', get_user_broadcast, name='get_user_broadcast'),
]
