from authentication.models import Profile
from django.db import models
from utils.constants import DocumentType

import uuid


class Grower(models.Model):
    """Modelo de Produtor/Hortleão.
    Uma instância deste modelo representa um Produtor/Hortelão.
    
    Atributos:
        - id (uuid.UUID): ID do produtor gerado ao salvar e não editável.
        - name (str): Nome do produtor.
        - document (str): Documento do produtor.
        - documentType (str): Tipo de documento do produtor baseado em contants do arquivo [contants.DocumentType](../../../utils/constants#service.src.utils.constants.DocumentType).
        - profile (Profile): Perfil de Usuário do produtor.
    """
    
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=100)

    document = models.CharField("Document", max_length=20)
    documentType = models.CharField(
        "Document Type",
        max_length=1,
        choices=[
            (documentType.value, documentType.name) for documentType in DocumentType
        ],
        default=DocumentType.CPF.value,
    )
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        verbose_name="Profile",
        related_name="grower",
        related_query_name="grower",
    )

    def __str__(self):
        return f"{self.profile.get_full_name()} ({self.profile.username})"

    class Meta:
        verbose_name = "Grower"
        verbose_name_plural = "Growers"
