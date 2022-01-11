
from django.db import models

from guitarradar.utils.models import BaseModel


class GuitarBaseModel(BaseModel):
    """Base model with common fields for guitars and its components.
    """

    approved = models.BooleanField(default=False, null=False, blank=True)
    brand = models.ForeignKey('guitars.Brand', on_delete=models.PROTECT, null=False)
    model_name = models.CharField(max_length=300)
    origin = models.CharField(max_length=300)
    url = models.CharField(max_length=5000)

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['brand', 'model_name']
        unique_together = ['brand', 'model_name']

    def __str__(self) -> str:
        return f'{self.brand} {self.model_name}'
