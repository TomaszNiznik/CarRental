from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include(('cars.urls', 'cars'), namespace='cars')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

]
# Jeśli jesteśmy w trybie DEBUG, dodajemy konfigurację dla mediów (obrazy, pliki itp.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
