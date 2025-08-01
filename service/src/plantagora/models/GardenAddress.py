from django.db import models
from simple_history.models import HistoricalRecords

from plantagora.models import BaseAddress, Garden
from utils.constants import Status


class GardenAddress(BaseAddress):
    """Modelo de endereço.
    Uma instância deste modelo representa um endereço de uma Horta.

    Atributos:
        - id (uuid.UUID): ID do endereço gerado ao salvar e não editável.
        - garden (Garden): Horta a qual o endereço pertence.
        - street (str): Rua do endereço.
        - number (str): Número do endereço.
        - complement (str): Complemento do endereço.
        - zip_code (str): CEP do endereço.
        - city (str): Cidade do endereço.
        - state (str): Estado do endereço.
        - status (str): Status do endereço baseado em contants do arquivo
        [contants.Status](../../utils/constants.md#service.src.utils.constants.Status).
    """

    history = HistoricalRecords()

    garden = models.ForeignKey(
        Garden,
        on_delete=models.CASCADE,
        verbose_name="Garden",
        related_name="addresses",
        related_query_name="address",
    )

    status = models.IntegerField(
        verbose_name="Status",
        choices=Status.STATUS_CHOICES,
        default=Status.ACTIVE,
    )

    class Meta:
        verbose_name = "Endereço da Horta"
        verbose_name_plural = "Endereços das Hortas"

    def __str__(self):
        return f"{self.street}, {self.number} ({self.zip_code})- {self.city}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
