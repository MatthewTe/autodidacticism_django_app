from django.urls import path
from . import views

# Declaring the core url routes:
urlpatterns = [

    # Index Page Path:
    path('', views.index, name='index')

]
