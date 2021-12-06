
import logging

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views.generic import View

from guitarradar.utils import constants
from guitarradar.utils.exceptions import BusinessException
from .forms import LoginForm, SignupForm
from . import services


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


class Signup(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        form = SignupForm(prefix='signup')
        return render(request, 'users/signup.html', {'signup_form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = SignupForm(data=request.POST, prefix='signup')
        if form.is_valid():
            try:
                services.sign_up(
                    username=form.cleaned_data.get('username'),
                    email=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password')
                )
                messages.success(request, _('You have successfully signed up!'))
                return redirect('index:main')
            except BusinessException as e:
                messages.error(request, _(str(e)))
                return redirect('users:signup')
        else:
            logger.error(form.errors)
            messages.error(request, _(constants.FORM_ERROR_MSG))
        return redirect('index:main')
