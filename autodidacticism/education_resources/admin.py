from django.contrib import admin
# Importing App models to add to admin dashboard:
from .models import Resources_Index_Card

# Regestering the Education Resource Card Model:
admin.site.register(Resources_Index_Card)
