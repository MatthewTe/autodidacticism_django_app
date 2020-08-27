from django.shortcuts import render

# Importing Database Models to be used in views:
from .models import Resources_Index_Card

def resources_index(request):
    """
    The method that renders the index page for all educational content of the site.

    The method renders an html template 'resources_index.html' that contains
    routes to all of the educational content of the site. The method also extracts
    relevant data from the database about educational resources and passes said
    data to the html template, allowing it to dynamically display data about
    avalible files and posts.

    It queries the database for a Query Set of all 'Resources_Index_Cards' using
    the orm model. This data is then passed into the 'resources_index.html'
    template and is used to dynamically create resource cards.


    Args:
        request (http request): The http request that is sent to the server from
            the client.

    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.

    """
    # Querying all card data from the database using the "Resources_Index_Cards" model:
    resource_cards = Resources_Index_Card.objects.all()

    # Creating the context that will be used to pass data into the template:
    context = {
        'resource_cards' : resource_cards
    }

    return render(request, 'education_resources/resources_index.html', context=context)
