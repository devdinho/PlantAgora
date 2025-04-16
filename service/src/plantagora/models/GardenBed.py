import uuid

from django.db import models
from simple_history.models import HistoricalRecords

from plantagora.models import Garden, GardenAddress
from utils.constants import Status


class GardenBed(models.Model):
    """Modelo de canteiro.
    Uma instância deste modelo representa um canteiro de uma horta.

    Atributos:
        - id (uuid.UUID): ID do canteiro gerado ao salvar e não editável.
        - code (str): Código do canteiro gerado ao salvar e não editável.
        - garden (Garden): Horta a qual o canteiro pertence.
        - signature (Signature): Assinatura do canteiro.
        - status (str): Status do canteiro baseado em contants do arquivo
        [contants.Status](../../utils/constants.md#service.src.utils.constants.Status).
    """

    history = HistoricalRecords()

    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField("Code", max_length=10, unique=True, editable=False)

    garden = models.ForeignKey(
        Garden,
        on_delete=models.CASCADE,
        verbose_name="Garden",
        related_name="gardenBeds",
        related_query_name="gardenBed",
    )

    garden_address = models.ForeignKey(
        GardenAddress,
        on_delete=models.CASCADE,
        verbose_name="Garden Address",
        related_name="gardenBeds",
        related_query_name="gardenBed",
        null=True,
        blank=True,
    )

    signature = models.ForeignKey(
        "Signature",
        on_delete=models.CASCADE,
        verbose_name="Signature",
        related_name="gardenBeds",
        related_query_name="gardenBed",
    )

    status = models.IntegerField(
        "Status",
        choices=Status.STATUS_CHOICES,
        default=Status.ACTIVE,
    )

    class Meta:
        verbose_name = "Garden Bed"
        verbose_name_plural = "Garden Beds"

    def __str__(self):
        return "{} - {} ({})".format(self.code, self.garden, self.garden_address)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = f"C-{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)
