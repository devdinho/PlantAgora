from django.db import models
from plantagora.models import Garden, Grower
from utils.constants import Status
import uuid


class Signature(models.Model):
    """Modelo de assinatura.
    Uma instância deste modelo representa uma assinatura de um produtor em uma horta.
    
    Atributos:
        - id (uuid.UUID): ID da assinatura gerado ao salvar e não editável.
        - garden (Garden): Horta assinada.
        - grower (Grower): Produtor que assinou a horta.
        - status (str): Status da assinatura baseado em contants do arquivo [contants.Status](../../../utils/constants#service.src.utils.constants.Status).
        - releasedAt (datetime): Data de liberação da assinatura.
        - updatedAt (datetime): Data de atualização da assinatura.
        - endedAt (datetime): Data de término da assinatura.
    """
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    garden = models.ForeignKey(
        Garden,
        on_delete=models.CASCADE,
        verbose_name="Garden",
        related_name="signatures",
        related_query_name="signature",
    )
    grower = models.ForeignKey(
        Grower,
        on_delete=models.CASCADE,
        verbose_name="Grower",
        related_name="signatures",
        related_query_name="signature",
    )

    status = models.CharField(
        "Status",
        max_length=1,
        choices=[(status.value, status.name) for status in Status],
        default=Status.ACTIVE.value,
    )

    releasedAt = models.DateTimeField("Released At", auto_now_add=True)
    updatedAt = models.DateTimeField("Updated At", auto_now=True)
    endedAt = models.DateTimeField("Ended At", null=True, blank=True)

    class Meta:
        verbose_name = "Signature"
        verbose_name_plural = "Signatures"
