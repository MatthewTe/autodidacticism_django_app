from django.contrib import admin

# Importing web_core models to be added to the admin view:
from .models import Applications_Index_Cards


# Regestering the Applications_Index_Cards Model in Admin View:
admin.site.register(Applications_Index_Cards)
