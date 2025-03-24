from django.db import models
from utils.constants import Status

from plantagora.models import Garden

import uuid

class Address(models.Model):
  id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
  
  garden = models.ForeignKey(Garden, on_delete=models.CASCADE, verbose_name='Garden', related_name='addresses', related_query_name='address')
    
  street = models.CharField('Street', max_length=100)
  number = models.CharField('Number', max_length=10)
  
  complement = models.CharField('Complement', max_length=100, blank=True, null=True)
  
  zip_code = models.CharField('Zip Code', max_length=8)
  
  city = models.CharField('City', max_length=100)
  state = models.CharField('State', max_length=2)
  
  status = models.CharField('Status', max_length=1, choices=[(status.value, status.name) for status in Status], default=Status.ACTIVE.value)
  
  class Meta:
    verbose_name = 'Address'
    verbose_name_plural = 'Addresses'
  
  def __str__(self):
    return f'{self.street}, {self.number} - {self.city}/{self.state}'
  
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)