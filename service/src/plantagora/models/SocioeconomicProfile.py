from django.db import models
from simple_history.models import HistoricalRecords
from utils.constants import Status

import uuid
from datetime import datetime

class SocioeconomicProfile(models.Model):
  """Modelo representando um perfil socioeconômico de um horticultor.
  Este modelo é utilizado para armazenar as respostas de um horticultor a um questionário
  socioeconômico, incluindo o questionário associado, as respostas dadas e o status da resposta.
  Atributos:
    - id: Identificador único do perfil socioeconômico.
    - questionaire: Referência ao questionário socioeconômico respondido.
    - grower: Referência ao horticultor que respondeu ao questionário.
    - answers: Um objeto JSON contendo as respostas do horticultor ao questionário.
    - status: O status do questionario, que pode ser ativo ou inativo.
    - submitted_at: Data e hora em que o perfil foi submetido.
    - updatedAt: Data e hora da última atualização do perfil.
  """
  history = HistoricalRecords()

  id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)

  questionaire = models.ForeignKey(
    "SocioeconomicQuestionnaire",
    on_delete=models.CASCADE,
    related_name="profiles",
    verbose_name="Socioeconomic Questionnaire",
  )

  grower = models.ForeignKey(
    "Grower",
    on_delete=models.CASCADE,
    related_name="socioeconomic_profiles",
    verbose_name="Grower",
  )
  
  answers = models.JSONField(
    "Answers",
    default=dict,
    help_text="A JSON object containing the answers to the questionnaire.",
  )
  
  status = models.IntegerField(
    "Status",
    choices=Status.STATUS_CHOICES,
    default=Status.ACTIVE,
  )

  submitted_at = models.DateTimeField("Submitted At", default=datetime.now)
  updatedAt = models.DateTimeField("Updated At", auto_now=True)

  class Meta:
    verbose_name = "Socioeconomic Profile"
    verbose_name_plural = "Socioeconomic Profiles"
    unique_together = (("questionaire", "grower"),)
    ordering = ["-submitted_at"]