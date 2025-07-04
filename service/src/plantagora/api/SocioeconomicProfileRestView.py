from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from plantagora.models import SocioeconomicProfile
from plantagora.serializers import SocioeconomicProfileSerializer


class SocioeconomicProfileRestView(viewsets.ModelViewSet):
    """Endpoint para gerenciar perfis socioeconômicos.

    Permite listar, criar, atualizar e excluir perfis socioeconômicos.
    Apenas usuários autenticados podem acessar este endpoint.
    """

    permission_classes = [IsAuthenticated]
    queryset = SocioeconomicProfile.objects.all().order_by("-updatedAt")
    serializer_class = SocioeconomicProfileSerializer
    http_method_names = [
        "get",
        "post",
        "put",
    ]
