from django.db.models import BooleanField

from .base import GuitarBaseModel


class Pickup(GuitarBaseModel):

    active = BooleanField(default=False)
