from django.shortcuts import render

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
