from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('i18n/setlang', include('django.conf.urls.i18n')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)