from django.urls import path, re_path
from . import views

# Declaring resources url routes:
urlpatterns = [

    # Educational Resources Index Path:
    path('', views.resources_index, name='resources_index'),

    # Educational Resources Article Index Page:
    path('articles/<str:category>', views.resources_article_index,
        name='resources_article_index_category_filtered'),
    path('articles/', views.resources_article_index, name='resources_article_index'),

    # Path for individual articles based on input slug values:
    path('article_display/<slug:slug>', views.resources_article_display, name='article_display'),

    # Path for the Resources Catalogue Index Page:
    path('catalogue/<str:category>', views.catalogue_index,
        name='resources_catalogue_index_category_filtered'),
    path('catalogue/', views.catalogue_index, name='catalogue_index')

]
