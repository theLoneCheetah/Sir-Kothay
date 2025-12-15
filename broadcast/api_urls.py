from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import BroadcastMessageViewSet

router = DefaultRouter()
router.register(r'messages', BroadcastMessageViewSet, basename='broadcastmessage')

urlpatterns = [
    path('', include(router.urls)),
]
