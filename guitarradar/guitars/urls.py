from django.urls import path

from .views import guitar_detail, brand_detail


urlpatterns = [
    path('guitar/', guitar_detail, name='guitar_detail'),
    path('brand/', brand_detail, name='brand_detail')
]
