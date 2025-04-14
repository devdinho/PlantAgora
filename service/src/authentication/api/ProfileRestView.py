from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from authentication.serializers import ProfileSerializer
from authentication.models import Profile

class ProfileRestView(viewsets.ModelViewSet):
    """Endpoint para registrar um novo usuário.
    
        Payload:
        ```json
            {
                "first_name": "string",
                "last_name": "string",
                "username": "string",
                "password": "string",
                "email": "string",
            }
        ```
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.none()
    
    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)
    
    def create(self, request, *args, **kwargs):
        raise Exception("Create not allowed")
    
    def list(self, request):
        data = Profile.objects.filter(id=request.user.id)
        if data:
            profile = ProfileSerializer(instance=data, many=True).data[0]
        else:
            raise Exception("Profile not found")

        return Response(profile, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):        
        instance = Profile.objects.get(id=kwargs.get('pk'))
        
        if instance.id != kwargs['pk'] and not request.user.is_superuser:
            raise Exception("You can only update your own profile!")
        
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        raise Exception("Delete not allowed")