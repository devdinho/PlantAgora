from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from plantagora.models import SocioeconomicQuestionnaire
from plantagora.serializers import SocioeconomicQuestionnaireSerializer


class SocioeconomicQuestionnaireRestView(viewsets.ModelViewSet):
    """Endpoint para gerenciar questionários socioeconômicos.

    Permite listar, criar, atualizar e excluir questionários.
    Apenas usuários autenticados podem acessar este endpoint.
    """

    permission_classes = [IsAuthenticated]
    queryset = SocioeconomicQuestionnaire.objects.all().order_by("-releasedAt")
    serializer_class = SocioeconomicQuestionnaireSerializer
    http_method_names = ["get", "post", "put"]
