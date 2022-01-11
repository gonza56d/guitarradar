from django import forms

from guitarradar.guitars.models import Bridge


class CreateBridgeForm(forms.ModelForm):

    class Meta:
        model = Bridge
        exclude = ['approved']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
