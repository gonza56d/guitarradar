from django import forms

from guitarradar.guitars.models import Guitar, Brand


class CreateGuitarForm(forms.ModelForm):

    class Meta:
        model = Guitar
        exclude = ['approved', 'overall_score', 'pricepoint_score']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['brand'].widget = forms.Select(
            attrs={'class': 'form-control'},
            choices=(
                (brand, brand.name)
                for brand in Brand.objects.filter(approved=True)
            )
        )

