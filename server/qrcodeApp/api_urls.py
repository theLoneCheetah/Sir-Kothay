from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import QRCodeViewSet

router = DefaultRouter()
router.register(r'qrcodes', QRCodeViewSet, basename='qrcode')

urlpatterns = [
    path('', include(router.urls)),
]
