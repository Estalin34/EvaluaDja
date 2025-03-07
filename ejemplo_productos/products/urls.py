from django.urls import path
from .views import driver_list, driver_detail

urlpatterns = [
    path('', driver_list, name='driver_list'),
    path('driver/<int:driver_id>/', driver_detail, name='driver_detail'),
]
