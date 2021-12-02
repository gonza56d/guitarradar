
from django.contrib import auth
from django.http import HttpRequest


def login(request: HttpRequest, username: str, password: str) -> bool:
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return True
    return False
