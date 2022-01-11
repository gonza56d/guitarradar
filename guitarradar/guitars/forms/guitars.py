from django import forms

from guitarradar.guitars.models import Guitar


class CreateGuitarForm(forms.ModelForm):

    class Meta:
        model = Guitar
        exclude = ['approved', 'overall_score', 'pricepoint_score']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
