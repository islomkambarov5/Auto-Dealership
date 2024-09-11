from django.urls import path
from .views import *

urlpatterns = [
    path('', CarsList.as_view(), name='index')
]
