from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import View

from guitarradar.guitars.forms.guitars import CreateGuitarForm
from guitarradar.guitars.models import Guitar


class CreateGuitarView(View):

    context = {
        'form': CreateGuitarForm(),
        'url': 'content:create_guitar',
        'kind': _('guitar')
    }

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request, 'guitars/creation.html', CreateGuitarView.context
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = CreateGuitarForm(data=request.POST)
        if form.is_valid():
            pickup = Guitar(**form.cleaned_data)
            pickup.save()
            return render(
                request,
                'guitars/creation.html',
                CreateGuitarView.context
            )


def guitar_detail(request):
    guitar = Guitar.objects.get(
        brand__name=request.GET.get('brand'),
        model_name=request.GET.get('model_name')
    )
    return render(request, 'guitars/guitar.html', {'guitar': guitar})
