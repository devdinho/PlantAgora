from django.db import models
from plantagora.models import Garden, Grower
from utils.constants import Status
import uuid


class Signature(models.Model):
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
