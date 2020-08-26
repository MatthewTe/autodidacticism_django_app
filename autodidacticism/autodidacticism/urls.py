"""autodidacticism URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Default Admin Implementation:
    path('admin/', admin.site.urls),

    # Core Web Application Routes (Basic navigation pages):
    path('', include('web_core.urls')),

    # Educational Resources Routes:
    path('resources/', include('education_resources.urls')),

    # Data APIs:
    path('data_api/', include('data_api.urls'))
]
