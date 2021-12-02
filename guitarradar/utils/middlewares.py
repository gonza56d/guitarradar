
from guitarradar.users.forms import LoginForm, SignupForm


class AuthFormsMiddleware:
    """Set LoginForm and SignupForm available in any request if user is not authenticated."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            request.login_form = LoginForm(prefix='login')
            request.signup_form = SignupForm(prefix='signup')
        return self.get_response(request)
