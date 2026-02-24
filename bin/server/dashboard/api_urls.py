from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import UserDetailsViewSet

router = DefaultRouter()
router.register(r'user-details', UserDetailsViewSet, basename='userdetails')

urlpatterns = [
    path('', include(router.urls)),
]
