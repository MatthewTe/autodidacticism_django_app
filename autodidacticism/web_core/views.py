from django.shortcuts import render
from django.http import HttpResponse

# Importing database models:
from .models import Applications_Index_Cards


def index(request):
    """
    The index method renders the main index ('home') page of the site.

    The method renders the index.html web template, which largely contains
    static data as the 'web_core' application exists mainly to serve as a
    'connecting node' for all other applications in the web app.

    Args:
        request (http request): The http request that is sent to the server from
            the client.

    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.

    """
    return render(request, 'web_core/index.html')

def applications_index(request):
    """
    The method that renders the index page that lists the avalible applications for
    the site.

    The method renders the 'applications_index.html' web template which contains
    information about all the current applications available on the site as well
    as routes to each applications. It queries the database for a Query Set of
    all 'Applications_Index_Cards' using the orm model. This data is then passed
    into the 'applications_index.html' template and is used to dynamically create
    application pages.

    Args:
        request (http request): The http request that is sent to the server from
            the client

    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.

    """
    # Extracting QuerySet of all Applications_Index_Cards objects from db:
    application_cards = Applications_Index_Cards.objects.all()

    # Building Context Dict for template:
    context = {
        'application_cards' : application_cards
    }

    return render(request, 'web_core/applications_index.html', context=context)
