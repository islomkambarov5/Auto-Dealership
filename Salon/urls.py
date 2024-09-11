from django.urls import path
from .views import *

urlpatterns = [
    path('', CarsList.as_view(), name='index'),
    path('car/detail/<slug:slug>', CarDetail.as_view(), name='car_detail')
]
