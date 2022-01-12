
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        'admin_panel/',
        include(
            ('guitarradar.adminpanel.urls', 'adminpanel'),
            namespace='adminpanel'
        )
    ),

    path('', include(('guitarradar.index.urls', 'index'), namespace='index')),

    path(
        'content/',
        include(('guitarradar.guitars.urls', 'guitars'), namespace='content')
    ),

    path(
        'users/',
        include(('guitarradar.users.urls', 'users'), namespace='users')
    ),
]
