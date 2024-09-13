from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('contact/', include('main.urls')),
    path('about/', include('main.urls')),
    path('services/', include('main.urls')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Подключение приложения main
]

# Подключение статических файлов только в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
