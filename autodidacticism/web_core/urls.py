from django.urls import path
from . import views

# Declaring the core url routes:
urlpatterns = [

    # Index Page Path:
    path('', views.index, name='index'),
    # Application Index Page Path:
    path('app_index', views.applications_index, name='applications_index')

]
