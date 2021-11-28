
from django.db.models import CharField


class DescriptiveCharField(CharField):

    def __init__(self, description: str = '', *args, **kwargs):
        self.description = description
        super().__init__(*args, **kwargs)
