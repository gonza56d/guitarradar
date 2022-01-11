from django import forms

from guitarradar.guitars.models import Brand


class CreateBrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        exclude = ['approved']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
