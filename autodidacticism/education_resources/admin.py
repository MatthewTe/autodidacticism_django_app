from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

# Importing App models to add to admin dashboard:
from .models import Resources_Index_Card, Article, CatalogueElement

# Regestering the Education Resource Card with custom Admin Model:
@admin.register(Resources_Index_Card)
class Resources_Index_Card_Admin(admin.ModelAdmin):
    """A custom admin model for the Resources_Index_Card admin.

    The model adds custom display fields to the admin dashboard for the Resources_Index_Card
    database model.

    Attributes:
        list_display (tuple): A tuple containing the model fields that are displayed
            on the Admin index page for the Resources_Index_Card model.

    """
    list_display = ('card_title', 'card_category')

# Regestering the Article Data Model with custom Admin Model:
@admin.register(Article)
class ArticleAdmin(MarkdownxModelAdmin):
    """A custom Admin Model for the Article Data Model.

    It Customizes the Form displayed in the Admin dashboard for the Article data
    model. In addition for customizing the 'fields' and 'list_display' values,
    the Admin Model inherits from the MarkdownxModelAdmin object, allowing a
    real time markdown field to be displayed on the admin dashboard.

    Attributes:

        fields (tuple): A tuple containing the model fields to be displayed in the
            admin form.

        list_display (tuple): A tuple containing the model fields that are displayed
            on the Admin index page for the Article model.

        list_filter (tuple): A tuple containing the model fields that can be used
            to filter all Article instances in the Admin index dashboard.

        search_fields (tuple): A tuple containing the model fields that can be
            used to search for an Article instance in the Admin index dashboard.
    """

    # Manually adding all fields of Article model to the Admin Index Page:
    fields = (
        'title',
        'author',
        'content',
        'main_category',
        'slug',
        'categories')

    # Showing the Title, Date Created and Author in the Admin Index:
    list_display = ('title', 'created_date', 'author')

    # Adding the posted_on and last_updated fields to be the main filters in the Admin Index:
    list_filter = ('created_date', 'last_updated')

    # Allowing the title field to be the main searchable field in the Admin Index:
    search_fields = ('title',)

# Regestering the CatalogueElement Data Model with custom Admin Model:
@admin.register(CatalogueElement)
class CatalogueElementAdmin(admin.ModelAdmin):
    """A custom admin model for the CatalogueElement database model.

    The model adds custom display fields to the admin dashboard for the CatalogueElement
    database model.

    Attributes:
        list_display (tuple): A tuple containing the model fields that are displayed
            on the Admin index page for the CatalogueElement model.

    """
    list_display = ('title', 'category', 'source', 'file')
