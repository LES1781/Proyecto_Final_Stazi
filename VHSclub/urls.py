"""VHSclub URL Configuration"""

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from vhsApp.views import inicio


urlpatterns = [

    path('', inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('vhsApp/', include('vhsApp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
