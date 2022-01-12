from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import View

from guitarradar.guitars.forms.brands import CreateBrandForm
from guitarradar.guitars.models import Brand


class CreateBrandView(View):

    context = {
        'form': CreateBrandForm(),
        'url': 'content:create_brand',
        'kind': _('brand')
    }

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request, 'guitars/creation.html', CreateBrandView.context
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = CreateBrandForm(data=request.POST)
        if form.is_valid():
            bridge = Brand(**form.cleaned_data)
            bridge.save()
            return render(
                request,
                'guitars/creation.html',
                CreateBrandView.context
            )


def brand_detail(request):
    brand = Brand.objects.get(
        brand__name=request.GET.get('brand')
    )
    return render(request, 'guitars/brand.html', {'brand': brand})
