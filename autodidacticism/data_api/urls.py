from django.urls import path
from . import views

# Declaring resources url routes:
urlpatterns = [

    # Homepage Path:
    path('', views.data_api_index, name='data_api_index')

]
