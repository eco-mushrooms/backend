from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static


def health_check(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/mushroom/', include('microcontroller.urls')),
    path('api/farm/', include('farm.urls')),
    path('health-check/', health_check),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
