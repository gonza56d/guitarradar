from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import View

from guitarradar.guitars.forms.bridges import CreateBridgeForm
from guitarradar.guitars.models import Bridge


class CreateBridgeView(View):

    context = {
        'form': CreateBridgeForm(),
        'url': 'content:create_bridge',
        'kind': _('bridge')
    }

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request, 'guitars/creation.html', CreateBridgeView.context
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = CreateBridgeForm(data=request.POST)
        if form.is_valid():
            bridge = Bridge(**form.cleaned_data)
            bridge.save()
            return render(
                request,
                'guitars/creation.html',
                CreateBridgeView.context
            )
