from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Place


def index(request):
    features = {
        'type': 'FeatureCollection',
        'features': [],
    }
    for place in Place.objects.prefetch_related('images').all():
        features['features'].append({
            'type': 'Feature',
            'geometry': place.get_point(),
            'properties': place.get_properties(request),
        })
    return render(request, 'core/index.html', context={'features': features})


def api_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return JsonResponse(place.get_properties(request))
