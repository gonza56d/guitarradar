
import logging

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from guitarradar.utils import constants
from .forms import LoginForm, SignupForm
import services


logger = logging.getLogger(__name__)


def login(request: HttpRequest) -> HttpResponse:
    form = LoginForm(data=request.POST, prefix='login')
    if form.is_valid():
        logged_in = services.login(
            request=request,
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password')
        )
        if logged_in:
            messages.success(request, _('You have logged in'))
        else:
            messages.warning(request, _('Wrong credentials'))
    else:
        logger.error(form.errors)
        messages.error(request, _(constants.FORM_ERROR_MSG))
    return redirect('index:main')


def logout(request: HttpRequest) -> HttpResponse:
    logged_out = services.logout(request)
    if logged_out:
        messages.success(request, _('You have logged out'))
    return redirect('index:main')


def signup(request: HttpRequest) -> HttpResponse:
    form = SignupForm(data=request.POST, prefix='signup')
    if form.is_valid():
        signed_up = services.sign_up(
            username=form.cleaned_data.get('username'),
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password')
        )
        if signed_up:
            messages.success(request, _('You have successfully signed up!'))
        else:
            messages.warning(request, '#TODO')
    else:
        logger.error(form.errors)
        messages.error(request, _(constants.FORM_ERROR_MSG))
    return redirect('index:main')
