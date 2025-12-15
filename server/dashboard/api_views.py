from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserDetails
from .serializers import UserDetailsSerializer


class UserDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint for user details management
    """
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Filter queryset to only show authenticated user's details"""
        if self.request.user.is_staff:
            return UserDetails.objects.all()
        return UserDetails.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_details(self, request):
        """Get current user's details"""
        try:
            user_details = UserDetails.objects.get(user=request.user)
            serializer = UserDetailsSerializer(user_details)
            return Response(serializer.data)
        except UserDetails.DoesNotExist:
            return Response({'error': 'User details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['put', 'patch'], permission_classes=[IsAuthenticated])
    def update_my_details(self, request):
        """Update current user's details"""
        try:
            user_details = UserDetails.objects.get(user=request.user)
            serializer = UserDetailsSerializer(user_details, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserDetails.DoesNotExist:
            return Response({'error': 'User details not found'}, status=status.HTTP_404_NOT_FOUND)
