import uuid

from django.db import models
from simple_history.models import HistoricalRecords

from authentication.models import Profile
from plantagora.models import BaseAddress
from utils.constants import DocumentType, LevelOfEducation


class Grower(models.Model):
    """Modelo de Produtor/Hortleão.
    Uma instância deste modelo representa um Produtor/Hortelão.

    Atributos:
        - id (uuid.UUID): ID do produtor gerado ao salvar e não editável.
        - name (str): Nome do produtor.
        - document (str): Documento do produtor.
        - documentType (int): Tipo de documento do produtor baseado em contants do arquivo
        [contants.DocumentType](../../utils/constants.md#service.src.utils.constants.DocumentType).
        - profile (Profile): Perfil de Usuário do produtor.
    """

    history = HistoricalRecords()

    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)

    caf = models.CharField(
        "CAF",
        max_length=9,
        help_text="Cadastro Nacional da Agricultura Familiar ou ao Número de Autorização Centralizada",
        blank=True,
        null=True,
    )

    address = models.ForeignKey(
        BaseAddress,
        on_delete=models.CASCADE,
        verbose_name="Address",
        null=True,
        blank=True,
    )

    levelOfEducation = models.IntegerField(
        "Level of Education",
        choices=LevelOfEducation.LEVEL_OF_EDUCATION_CHOICES,
        default=LevelOfEducation.BASIC,
    )

    document = models.CharField("Document", max_length=20)
    documentType = models.IntegerField(
        "Document Type",
        choices=DocumentType.DOCUMENT_TYPE_CHOICES,
        default=DocumentType.CPF,
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name="Profile",
    )

    def __str__(self):
        return f"{self.profile.get_full_name()} ({self.profile.username})"

    class Meta:
        verbose_name = "Grower"
        verbose_name_plural = "Growers"
