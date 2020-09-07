from django.shortcuts import render
from django.db.models import Q

# Importing Database Models to be used in views:
from .models import Resources_Index_Card, Article

# Importing 3rd party packages:
from functools import reduce
import operator

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

def resources_article_index(request, category='all'):
    """The method renders the articles_index.html template with article data from the database.

    The articles_index.html template is rendered, along with article data read from
    the Article data model. On the front end, search queries can be input by the
    user via input from a search input form. These query parameters are passed
    into the request parameter as a string in the form of the ['q'] parameter and
    a category parameter passed directly into the url path.

    There are two url paths that trigger this route:

    * re_path(r'^articles/', views.resources_article_index, name='resources_article_index'),
    * re_path(r'^articles/<str:category>/', views.resources_article_index,
        name='resources_article_index_category')

    When no category parameter is probvided in the url, the first path 'resources_article_index'
    calls this method without passing a category parameter. As such the method uses
    the default category parameter specified: 'all'. If the url path contains a
    category parameter then the second path 'resources_article_index_category' is
    used to call this method, passing the url category parameter into the method.

    This method applies the necessary logic to only pass instances of the Article
    model that fit the user input search parameter. The article search logic is
    as follows:

    1) If there is no category parameter (category='all') then no inital filter
        is placed on the Article QuerySet and only the query parameter is used
        to filter down the Article QuerySet.

    2) If there is a url category parameter then this parameter is used to filter
        the Article QuerySet against the Article.main_category parameter. This
        filtered QuerySet is then passed onto the logic that further filters it
        based on the 'q' query parameters.

    3) If there is no query parameter (the user has not searched anything or it is
        a 'fresh' article index page) then all of the Article instances are queried
        and passed into the template, orderd by most recent.

    4) If query parameters are present (meaning the user has made a search) then
        the q key-word-argument string is split into a list of strings based on
        the spacing of the string (done via .split(" ")) and each of these strings
        are used to create query filters for the Article model based on Article
        categories and titles. Any Article's that are queried with these filters
        are then passed into the template.

    Other front-end elements are rendered based on data that is statically queried
    from the backend such as the 'Article Categories' div element that is displayed
    using data extracted from the Resources_Index_Card model. This Article Category
    element uses href links that pass the category url parameter into this view.
    Which dictates which articles could be displayed.

    References:
        * https://docs.djangoproject.com/en/3.1/topics/http/urls/
        * https://www.kobrien.me/blog/post/building-simple-search-django/
        * https://django-book.readthedocs.io/en/latest/chapter08.html
        * https://learndjango.com/tutorials/django-search-tutorial
        * https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query
        * https://stackoverflow.com/questions/9304908/how-can-i-filter-a-django-query-with-a-list-of-values
        * https://django-filter.readthedocs.io/en/stable/guide/usage.html#the-view
        * https://stackoverflow.com/questions/11508744/django-models-filter-by-foreignkey

    Args:
        request (http request): The http request that is sent to the server from
            the client.

        category (str): The category used to filter the type of articles displayed.
            If no category is provided then default value of 'all' is provided
            and no category filter is applied to articles.

    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.

    Todo:
        * Change basic query functionality to a more advanced search such as
            elasticsearch or using django-filters (see refrences).
    """
    # Creating the full QuerySet of Resource Index Cards and Article models:
    article_cards = Resources_Index_Card.objects.all()
    articles = Article.objects.all()

    # Parsing Potential Url Query:

    # First Parsing the Potential 'category' parameter used to select articles via hrefs:
    if category != 'all' and category.strip():

        # Declaring the inital Article QuerySet based on a category variable:
        category_string = category

        # Creating inital query set:
        articles = articles.filter(
            main_category__card_category=category_string
            )

    # If there are url queries, perform filtered Article search on 'articles' QuerySet:
    if ('q' in request.GET) and request.GET['q'].strip():

        # Declaring query string:
        query_string = request.GET['q']

        # Splitting the query string into a list of queries via white space:
        query_lst = [query for query in query_string.split(" ")]

        # Using the Complex Lookup object Q to query Articles based on queries list:
        articles = articles.filter(
            # Using reduce to match each element of the queries_lst with Article fields:
            reduce(operator.and_, (Q(title__contains=query) for query in query_lst))
            )

    # Creating context to be passed into the template:
    context = {
        'articles' : articles,
        'article_categories': article_cards
        }

    return render(request, "education_resources/articles_index.html", context=context)

def resources_article_display(request, slug):
    """This method renders the 'individual_article.html' template and passes data
    from a single instance of the Article data model into the template.

    This is the view model responsible for rendering individual articles. The
    query parameter <slug:slug> in the url is passed into the method as the parameter
    'slug'. The slug parameter is used to create a QuerySet of a single Article
    instance that contains the single article that matches the slug parameter. This
    article is passed into the template.

    Args:
        slug (str): The slug parameter that is passed into the method from the url
            path. It is used to query the specific Article data model instance.

    Returns:
        django.shortcuts.render: The django template rendered as html with full
            context.

    """
    # Querying the Article data model that matches the slug parameter:
    article = Article.objects.filter(slug=slug).first()

    # Creating a context containing data to pass into the template:
    context = {
        'article' : article,
    }

    return render(request, 'education_resources/individual_article.html', context=context)
