from django import forms
from django.utils.translation import gettext as _

from guitarradar.guitars.models import Pickup


class CreatePickupForm(forms.ModelForm):

    class Meta:
        model = Pickup
        exclude = ['approved']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['active'].widget = forms.Select(
            attrs={'class': 'form-control'},
            choices=[(True, _('Yes')), (False, _('No'))]
        )
