from django.db import models

from plantagora.models import Garden, Signature

from utils.constants import Status
import uuid

class GardenBed(models.Model):
  id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
  code = models.CharField('Code', max_length=10, unique=True, editable=False)
  
  garden = models.ForeignKey(Garden, on_delete=models.CASCADE, verbose_name='Garden', related_name='gardenBeds', related_query_name='gardenBed')
  signature = models.ForeignKey(Signature, on_delete=models.CASCADE, verbose_name='Signature', related_name='gardenBeds', related_query_name='gardenBed')
  
  status = models.CharField('Status', max_length=1, choices=[(status.value, status.name) for status in Status], default=Status.ACTIVE.value)
  
  class Meta:
    verbose_name = 'Garden Bed'
    verbose_name_plural = 'Garden Beds'
  
  def __str__(self):
    return self.name
  
  def save(self, *args, **kwargs):
    if not self.code:
      self.code = f'B-{uuid.uuid4().hex[:8]}'
    super().save(*args, **kwargs)