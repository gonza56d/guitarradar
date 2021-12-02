
import logging

from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from .forms import LoginForm
import services


logger = logging.getLogger(__name__)


def login(request):
    login_form = LoginForm(data=request.POST, prefix='login')
    if login_form.is_valid():
        login_success = services.login(
            request=request,
            username=login_form.cleaned_data.get('username'),
            password=login_form.cleaned_data.get('password')
        )
        if login_success:
            messages.success(request, _('You have logged in'))
        else:
            messages.warning(request, _('Wrong credentials'))
    else:
        logger.error(login_form.errors)
        messages.error(request, _('Something went wrong, please contact support'))
    return redirect('index:main')
