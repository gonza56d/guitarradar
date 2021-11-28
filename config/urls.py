
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('guitarradar.index.urls', 'index'), namespace='index')),
]
