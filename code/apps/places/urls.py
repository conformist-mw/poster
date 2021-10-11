from django.urls import path

from .views import index, api_place

urlpatterns = [
    path('', index, name='index'),
    path('places/<int:place_id>/', api_place, name='api_place'),
]
