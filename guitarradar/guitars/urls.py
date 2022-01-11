from django.urls import path

from guitarradar.guitars.views import (
    brand_detail,
    CreateBrandView,
    CreateBridgeView,
    CreateGuitarView,
    guitar_detail,
)
from guitarradar.guitars.views.pickups import CreatePickupView

urlpatterns = [
    path('brands/', brand_detail, name='brand_detail'),
    path('brands/create/', CreateBrandView.as_view(), name='create_brand'),

    path('bridges/create/', CreateBridgeView.as_view(), name='create_bridge'),

    path('guitars/', guitar_detail, name='guitar_detail'),
    path('guitars/create/', CreateGuitarView.as_view(), name='create_guitar'),

    path('pickups/create/', CreatePickupView.as_view(), name='create_pickup'),
]
