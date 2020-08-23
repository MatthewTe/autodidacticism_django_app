"""autodidacticism URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Default Admin Implementation:
    path('admin/', admin.site.urls),

    # Core Web Application Routes (Basic navigation pages):
    path('', include('web_core.urls'))
]
