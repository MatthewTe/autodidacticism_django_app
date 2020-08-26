from django.urls import path
from . import views

# Declaring resources url routes:
urlpatterns = [

    # Homepage Path:
    path('', views.resources_index, name='resources_index')

]
