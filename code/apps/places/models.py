from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField(blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(upload_to='images')
    place = models.ForeignKey(
        to=Place, related_name='images', on_delete=models.CASCADE,
    )
