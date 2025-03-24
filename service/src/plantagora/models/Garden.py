from django.db import models
from utils.constants import Status
import uuid


class Garden(models.Model):
    name = models.CharField("Name", max_length=100)
    code = models.CharField("Code", max_length=10, unique=True, editable=False)
    status = models.CharField(
        "Status",
        max_length=1,
        choices=[(status.value, status.name) for status in Status],
        default=Status.ACTIVE.value,
    )

    class Meta:
        verbose_name = "Garden"
        verbose_name_plural = "Gardens"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = f"G-{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)
