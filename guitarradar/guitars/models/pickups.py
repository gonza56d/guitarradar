
from django.db import models

from guitarradar.utils.models import BaseModel


class Pickup(BaseModel):

    approved = models.BooleanField(default=False, null=False, blank=True)
    brand = models.ForeignKey('guitars.Brand', on_delete=models.PROTECT, null=False)
    model_name = models.CharField(max_length=300)
    origin = models.CharField(max_length=300)
    url = models.CharField(max_length=5000)

    class Meta:
        unique_together = ['brand', 'model_name']

    def __str__(self) -> str:
        return f'{self.brand} {self.model_name}'
