from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('token/', CreateTokenView.as_view(), name='token'),
]
