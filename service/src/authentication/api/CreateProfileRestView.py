from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from authentication.models import Profile
from authentication.serializers import ProfileSerializer
from django.http import JsonResponse


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

    permission_classes = [AllowAny]
    queryset = Profile.objects.all().order_by("-date_joined")
    serializer_class = ProfileSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        """Cria um novo usuário com os dados fornecidos no payload.

        Args:
            request: O objeto de solicitação HTTP.
            *args: Argumentos adicionais.
            **kwargs: Argumentos nomeados adicionais.

        Returns:
            Response: A resposta HTTP com os dados do usuário criado.
        """
        
        print(request.data)
        
        return JsonResponse({})
        return super().create(request, *args, **kwargs)