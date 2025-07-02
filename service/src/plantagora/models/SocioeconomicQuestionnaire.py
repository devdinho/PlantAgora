import uuid
from datetime import datetime

from django.db import models
from simple_history.models import HistoricalRecords

from utils.constants import Status


class SocioeconomicQuestionnaire(models.Model):
    """
    Modelo representando um questionário socioeconômico.
    Este modelo é utilizado para armazenar as perguntas e alternativas de um questionário
    que será aplicado aos horticultores para coletar informações socioeconômicas.

    Atributos:
      - id: Identificador único do questionário.
      - title: Título do questionário.
      - description: Descrição breve do questionário.
      - questions: Um objeto JSON contendo as perguntas e suas alternativas.
      - status: O status do questionário, que pode ser ativo ou inativo.
      - releasedAt: Data e hora em que o questionário foi liberado.
      - updatedAt: Data e hora da última atualização do questionário.
    """

    history = HistoricalRecords()

    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(
        "Title",
        max_length=255,
        help_text="The title of the socioeconomic questionnaire.",
    )

    description = models.TextField(
        "Description",
        blank=True,
        help_text="A brief description of the socioeconomic questionnaire.",
    )

    questions = models.JSONField(
        "Questions",
        default=dict,
        help_text="A JSON object containing the questions and their alternatives.",
    )

    status = models.IntegerField(
        "Status",
        choices=Status.STATUS_CHOICES,
        default=Status.ACTIVE,
    )

    releasedAt = models.DateTimeField("Released At", default=datetime.now)
    updatedAt = models.DateTimeField("Updated At", auto_now=True)

    class Meta:
        verbose_name = "Socioeconomic Questionnaire"
        verbose_name_plural = "Socioeconomic Questionnaires"
