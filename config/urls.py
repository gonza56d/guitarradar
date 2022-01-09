
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('guitarradar.index.urls', 'index'), namespace='index')),
    path(
        'guitars/',
        include(('guitarradar.guitars.urls', 'guitars'), namespace='guitars')
    ),
    path(
        'users/',
        include(('guitarradar.users.urls', 'users'), namespace='users')
    ),
]
