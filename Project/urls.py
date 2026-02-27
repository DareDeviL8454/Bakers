from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Bakers Gallery"
admin.site.site_title = "mini-project"
admin.site.index_title = "Welcome to Bakers Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls')),
]

# Serve media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)