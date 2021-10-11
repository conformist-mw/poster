from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    extra = 0
    model = PlaceImage
    readonly_fields = ['preview']

    # noinspection PyMethodMayBeStatic
    def preview(self, obj):
        return format_html(
            '<img src="{url}" style="max-height: 200px;" />',
            url=obj.image.url,
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (PlaceImageInline, )
