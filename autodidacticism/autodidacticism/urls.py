"""autodidacticism URL Configuration"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # Configuration urls:
    # -------------------
    # Configuring the urlpath to serve static files in development:
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

    # Adding MarkdownX application routes:
    url(r'^markdownx/', include('markdownx.urls')),

    # Admin autodocs application routes:
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Website Url Routes:
    # -------------------
    # Default Admin Implementation:
    path('admin/', admin.site.urls),

    # Core Web Application Routes (Basic navigation pages):
    path('', include('web_core.urls')),

    # Educational Resources Routes:
    path('resources/', include('education_resources.urls')),

    # Data APIs:
    path('data_api/', include('data_api.urls'))
]
