from django.contrib import admin

from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (PlaceImageInline, )
