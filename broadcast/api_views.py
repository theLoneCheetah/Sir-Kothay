from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import BroadcastMessage
from .serializers import BroadcastMessageSerializer


class BroadcastMessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for broadcast messages management
    """
    queryset = BroadcastMessage.objects.all()
    serializer_class = BroadcastMessageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Filter queryset to show user's own messages or all if staff"""
        if self.request.user.is_staff:
            return BroadcastMessage.objects.all().order_by('-id')
        return BroadcastMessage.objects.filter(user=self.request.user).order_by('-id')
    
    def perform_create(self, serializer):
        """Set the user when creating a broadcast message"""
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_messages(self, request):
        """Get current user's broadcast messages"""
        messages = BroadcastMessage.objects.filter(user=request.user).order_by('-id')
        serializer = BroadcastMessageSerializer(messages, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def active_message(self, request):
        """Get current user's active broadcast message"""
        try:
            message = BroadcastMessage.objects.get(user=request.user, active=True)
            serializer = BroadcastMessageSerializer(message)
            return Response(serializer.data)
        except BroadcastMessage.DoesNotExist:
            return Response({'error': 'No active message found'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def set_active(self, request, pk=None):
        """Set a message as active"""
        message = self.get_object()
        if message.user != request.user and not request.user.is_staff:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        
        message.active = True
        message.save()
        return Response({'message': 'Message set as active'})
