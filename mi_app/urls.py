from django.contrib import admin
from django.urls import path, include   # ← IMPORTANTE: añadir include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('timeline.urls')),   # ← Aquí agregas tu aplicación
]