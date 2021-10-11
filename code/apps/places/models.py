from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField(blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.title

    def get_point(self):
        return {
            'type': 'Point',
            'coordinates': [self.longitude, self.latitude]
        }

    def get_properties(self, request):
        images = [
            request.build_absolute_uri(image.image.url)
            for image in self.images.all()
        ]
        return {
            'title': self.title,
            'placeId': self.id,
            'imgs': images,
            'short_description': self.description_short,
            'long_description': self.description_long,
            'coordinates': {
                'lng': self.longitude,
                'lat': self.latitude,
            }
        }


class PlaceImage(models.Model):
    image = models.ImageField(upload_to='images')
    order = models.PositiveIntegerField(default=0)
    place = models.ForeignKey(
        to=Place, related_name='images', on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('order', )
