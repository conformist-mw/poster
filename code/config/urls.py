from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('test/', include(('apps.core.urls', 'apps.core'), namespace='core')),
    path('', include(('apps.places.urls', 'apps.places'), namespace='places')),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT,
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
