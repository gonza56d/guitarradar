
from django.urls import path

from .views import login, logout, Signup


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', Signup.as_view(), name='signup'),
]
