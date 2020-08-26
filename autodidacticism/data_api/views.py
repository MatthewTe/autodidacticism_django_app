from django.shortcuts import render


def data_api_index(request):
    """
    The method that renders the index page for all data api content on the site.

    The method renders an html template 'data_api_index.html' that contains
    routes to all of the educational content of the site. The method also extracts
    relevant data from the database about Data API resources and passes said
    data to the html template, allowing it to dynamically display data about
    avalible APIs and their documentation.

    Args:
        request (http request): The http request that is sent to the server from
            the client.

    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.

    """
    return render(request, 'data_api/data_api_index.html')
