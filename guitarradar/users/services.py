
from django.contrib import auth
from django.db.utils import IntegrityError
from django.http import HttpRequest

from guitarradar.utils.exceptions import BusinessException
from .models import User


def login(request: HttpRequest, username: str, password: str) -> bool:
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return True
    return False


def logout(request: HttpRequest) -> bool:
    if request.user.is_authenticated:
        auth.logout(request)
        return True
    return False


def sign_up(username: str, email: str, password: str) -> bool:
    try:
        if len(password) < 8:
            raise BusinessException('Password must have at least 8 characters')
        if len(username) < 3:
            raise BusinessException('Username must have at least 3 characters')
        user = User.objects.create_user(username=username, email=email, password=password)
        return True if user is not None else False
    except IntegrityError as e:
        if 'username' in str(e):
            raise BusinessException('Username already in use')
        if 'email' in str(e):
            raise BusinessException('Email already in use')
