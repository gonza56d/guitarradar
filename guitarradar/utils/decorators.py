from django.shortcuts import redirect


def admin_view(view):
    """Decorate a view function in order to allow it only for admins of any
    level."""

    def wrapper(request, *args, **kwargs):
        if not request.user.is_admin:
            return redirect('index:main')
        return view(request, *args, **kwargs)

    return wrapper
