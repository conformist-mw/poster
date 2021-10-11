from django.urls import path

from .views import api_place, index

urlpatterns = [
    path('', index, name='index'),
    path('places/<int:place_id>/', api_place, name='api_place'),
]
