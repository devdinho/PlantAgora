import uuid

from django.db import models
from simple_history.models import HistoricalRecords

from utils.models import City


class BaseAddress(models.Model):
    """Modelo Base de endereço.
    Uma instância deste modelo representa um endereço de uma Instância.

    Atributos:
        - id (uuid.UUID): ID do endereço gerado ao salvar e não editável.
        - street (str): Rua do endereço.
        - number (str): Número do endereço.
        - complement (str): Complemento do endereço.
        - zip_code (str): CEP do endereço.
        - city (str): Cidade do endereço.
    """

    history = HistoricalRecords()

    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)

    street = models.CharField("Street", max_length=100)

    number = models.CharField("Number", max_length=10)

    complement = models.CharField("Complement", max_length=100, blank=True, null=True)

    zip_code = models.CharField("Zip Code", max_length=8)

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name="City",
        related_name="addresses",
        related_query_name="address",
    )

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return f"{self.street}, {self.number} ({self.zip_code})- {self.city}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
