from rest_framework import viewsets

from authentication.serializers import ProfileSerializer
from authentication.models import Profile

class CreateProfileRestView(viewsets.ModelViewSet):
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
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer