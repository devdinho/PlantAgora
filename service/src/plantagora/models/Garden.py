import uuid

from django.db import models
from simple_history.models import HistoricalRecords

from utils.constants import Status


class Garden(models.Model):
    """Modelo de horta.
    Uma instância deste modelo representa uma horta.

    Atributos:
        - name (str): Nome da horta.
        - code (str): Código da horta gerado ao salvar e não editável.
        - status (str): Status da horta baseado em contants do arquivo
        [contants.Status](../../utils/constants.md#service.src.utils.constants.Status).
    """

    history = HistoricalRecords()

    name = models.CharField("Name", max_length=100)
    code = models.CharField("Code", max_length=10, unique=True, editable=False)
    status = models.IntegerField(
        verbose_name="Status",
        choices=Status.STATUS_CHOICES,
        default=Status.ACTIVE,
    )

    class Meta:
        verbose_name = "Garden"
        verbose_name_plural = "Gardens"

    def __str__(self):
        return "{}({})".format(self.name, self.code)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = f"H-{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)
