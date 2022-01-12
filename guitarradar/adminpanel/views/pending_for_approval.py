from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.views import View

from guitarradar.guitars.forms import CreateGuitarForm
from guitarradar.guitars.models import Brand, Bridge, Guitar, Pickup
from guitarradar.utils.decorators import admin_view


@admin_view
def list_peding_for_approval(request: HttpRequest) -> HttpResponse:
    context = {
        'brands': Brand.objects.filter(approved=False),
        'bridges': Bridge.objects.filter(approved=False),
        'guitars': Guitar.objects.filter(approved=False),
        'pickups': Pickup.objects.filter(approved=False)
    }
    return render(request, 'admin/list_pending_for_approval.html', context)


class CheckForApprovalGuitarView(View):

    @staticmethod
    @admin_view
    def get(request: HttpRequest) -> HttpResponse:
        guitar = Guitar.objects.get(
            brand__name=request.GET.get('brand'),
            model_name=request.GET.get('model_name')
        )
        context = {
            'form': CreateGuitarForm(instance=guitar),
            'kind': _('guitar'),
            'url': 'adminpanel:check_for_approval_guitar'
        }
        return render(request, 'admin/check_for_approval.html', context)

    @staticmethod
    @admin_view
    def post(request: HttpRequest) -> HttpResponse:
        form = CreateGuitarForm(**request.POST)
        if form.is_valid():
            Guitar.objects.filter(
                brand__name=request.POST.get('brand'),
                model_name=request.POST.get('model_name')
            ).update(**form.cleaned_data)
            return redirect('adminpanel:list_peding_for_approval')
