import uuid
from datetime import datetime

from django.db import models
from simple_history.models import HistoricalRecords

from plantagora.models import Garden
from utils.constants import SignatureValidationMonths, Status


class Signature(models.Model):
    """Modelo de assinatura.
    Uma instância deste modelo representa uma assinatura de um produtor em uma horta.

    Atributos:
        - id (uuid.UUID): ID da assinatura gerado ao salvar e não editável.
        - garden (Garden): Horta assinada.
        - grower (Grower): Produtor que assinou a horta.
        - status (str): Status da assinatura baseado em contants do arquivo
        [contants.Status](../../utils/constants.md#service.src.utils.constants.Status).
        - releasedAt (datetime): Data de liberação da assinatura.
        - updatedAt (datetime): Data de atualização da assinatura.
        - endedAt (datetime): Data de término da assinatura.
    """

    history = HistoricalRecords()

    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    garden = models.ForeignKey(
        Garden,
        on_delete=models.CASCADE,
        verbose_name="Garden",
        related_name="signatures",
        related_query_name="signature",
    )
    grower = models.ForeignKey(
        "Grower",
        on_delete=models.CASCADE,
        verbose_name="Grower",
        related_name="signatures",
        related_query_name="signature",
    )

    duration = models.IntegerField(
        "Duration",
        choices=SignatureValidationMonths.SIGNATURE_VALIDATION_MONTHS_CHOICES,
        default=SignatureValidationMonths.TWELVE_MONTHS,
    )

    status = models.IntegerField(
        "Status",
        choices=Status.STATUS_CHOICES,
        default=Status.ACTIVE,
    )

    releasedAt = models.DateTimeField("Released At", default=datetime.now)
    updatedAt = models.DateTimeField("Updated At", auto_now=True)

    class Meta:
        verbose_name = "Assinatura"
        verbose_name_plural = "Assinaturas"
