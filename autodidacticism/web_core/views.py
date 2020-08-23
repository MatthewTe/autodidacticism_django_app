from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    The index method renders the main index ('home') page of the site.

    The method renders the index.html web template, which largely contains
    static data as the 'web_core' application exists mainly to serve as a
    'connecting node' for all other applications in the web app.

    Args:
        request (http request): The http request that is sent to the server

    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.

    Todo:
        * Update index docstring as more dynamic rendering is added to the method.
    """
    return render(request, 'web_core/index.html')
