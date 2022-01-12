from django import forms

from guitarradar.guitars.models import Bridge, Brand


class CreateBridgeForm(forms.ModelForm):

    class Meta:
        model = Bridge
        exclude = ['approved']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['brand'].widget = forms.Select(
            attrs={'class': 'form-control'},
            choices=(
                (brand.id, brand.name)
                for brand in Brand.objects.filter(approved=True)
            )
        )
