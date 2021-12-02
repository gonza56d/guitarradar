
from django.db import models

from guitarradar.utils.models import BaseModel


class Brand(BaseModel):

    approved = models.BooleanField(default=False, null=False, blank=True)
    name = models.CharField(max_length=300, unique=True)
    url = models.CharField(max_length=5000)

    def __str__(self) -> str:
        return self.name
