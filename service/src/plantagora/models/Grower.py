import uuid

from django.db import models
from simple_history.models import HistoricalRecords

from authentication.models import Profile
from plantagora.models import BaseAddress
from utils.constants import Gender, LevelOfEducation


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

    document = models.CharField("Document", max_length=11, unique=True)

    gender = models.IntegerField(
        "Gender",
        choices=Gender.GENDER_CHOICES,
        default=Gender.OTHER,
    )

    birthDate = models.DateField(
        "Birth Date",
        help_text="Data de nascimento do produtor.",
        blank=True,
        null=True,
    )

    cell = models.CharField(
        "Cell",
        max_length=11,
        help_text="Número de celular do produtor.",
        blank=True,
        null=True,
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name="Profile",
    )

    registeredAt = models.DateTimeField(
        "Registered At", auto_now_add=True, editable=False, blank=True, null=True
    )

    updatedAt = models.DateTimeField(
        "Updated At", auto_now=True, editable=False, blank=True, null=True
    )

    registerApproved = models.BooleanField(
        "Register Approved",
        default=False,
        help_text="Indica se o registro do produtor foi aprovado.",
    )

    registerApprovedAt = models.DateTimeField(
        "Register Approved At", null=True, blank=True
    )

    registerApprovedBy = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name="Register Approved By",
        null=True,
        blank=True,
        related_name="approved_by",
    )

    def __str__(self):
        return f"{self.profile.get_full_name()} ({self.profile.username})"

    def save(self, *args, **kwargs):
        """Salva o objeto Grower e atualiza o campo registeredAt."""
        if not self.registeredAt:
            self.registeredAt = self.updatedAt

        if not self.registerApprovedAt and self.registerApproved:
            self.registerApprovedAt = self.updatedAt

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Grower"
        verbose_name_plural = "Growers"
