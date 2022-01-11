from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import View

from guitarradar.guitars.forms.pickups import CreatePickupForm
from guitarradar.guitars.models import Pickup


class CreatePickupView(View):

    context = {
        'form': CreatePickupForm(),
        'url': 'content:create_pickup',
        'kind': _('pickup')
    }

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request, 'guitars/creation.html', CreatePickupView.context
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = CreatePickupForm(data=request.POST)
        if form.is_valid():
            pickup = Pickup(**form.cleaned_data)
            pickup.save()
            return render(
                request,
                'guitars/creation.html',
                CreatePickupView.context
            )
