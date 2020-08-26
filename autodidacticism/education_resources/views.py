from django.shortcuts import render

# Create your views here.

def resources_index(request):
    """
    The method that renders the index page for all educational content of the site.

    The method renders an html template 'resources_index.html' that contains
    routes to all of the educational content of the site. The method also extracts
    relevant data from the database about educational resources and passes said
    data to the html template, allowing it to dynamically display data about
    avalible files and posts.

    Args:
        request (http request): The http request that is sent to the server from
            the client.

    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.

    """
    return render(request, 'education_resources/resources_index.html')
