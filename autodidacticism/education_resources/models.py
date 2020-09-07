from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Importing markdown Model Field:
from markdownx.models import MarkdownxField

# Importing 3-rd Party Packages:
from markdownify import markdownify
import markdown


class Resources_Index_Card(models.Model):
    """The Django Database model for educational resources Bootstrap cards.

    This class contains all the fields that contain the data necessary to construct
    an html bootstrap card on the front-end using Django's templating engine. In
    the application resources index page, a resource card contains the following main
    components:

    * A Card Head Image.
    * A Card Title.
    * A Description of the Application.
    * Two Buttons at the foot of the card, each containing:
        * Text
        * An Icon
        * An href Link
    * Metadata describing the application type of the card ('finance', 'web_framework',
    etc, etc.).

    Using Django Templates data is read from the database via this model and used
    to dynamically build card-decks. Dynamically building cards like this also
    allows cards to be created by inserting data in the admin dashboard.

    Attributes:

        card_image (models.CharField): The CharField representing the name of the image
            to be used in the card body.

        card_title (models.CharField): The CharField containing the title text of the
            card.

        card_description (models.TextField): The blob of text that is used as the main
            text body of the card.

        button_a_txt (models.CharField): The text of the first card button in the button
            group.

        button_a_icon (models.CharField): The CharField representing the name of the icon
            image to be attached to the button.

        button_b_txt (models.CharField): The text of the second card button in the button
            group.

        button_b_icon (models.CharField): The CharField representing the name of the icon
            image to be attached to the button.

        card_category (models.CharField): The string that will be used by the view logic
            or the django template to assign the card to a particular section of
            the html template.

    """
    # Card Body Content:
    card_image = models.CharField(
        max_length=100,
        help_text="The name of the image file to be included in the Card.",
        verbose_name="Card Image")
    card_title = models.CharField(
        max_length=100,
        help_text="The Title Text for the Card.",
        verbose_name="Card Title")
    card_description = models.TextField(
        help_text="The Long Description of the Card.",
        verbose_name="Card Description")
    # Button A Content:
    button_a_text = models.CharField(
        max_length=50,
        help_text='The main text content of the first button.',
        verbose_name="Button A Text")
    button_a_icon = models.CharField(
        max_length=50,
        # Setting the default icon value as 'posts_icon.png' in static/education_resources/images/icons:
        default = "posts_icon.png",
        help_text="The name of the icon image to be inserted into the first button.",
        verbose_name="Button A Icon")

    # Button B Content:
    button_b_text = models.CharField(
        max_length=50,
        help_text='The main text content of the second button.',
        verbose_name="Button B Text")
    button_b_icon = models.CharField(
        max_length=50,
        # Setting the default icon value as 'posts_icon.png' in static/education_resources/images/icons:
        default = "catalogue_icon.png",
        help_text="The name of the icon image to be inserted into the second button.",
        verbose_name="Button B Icon")

    # Defining the series of category choice fields:
    resource_categories = (
        ('Finance', 'finance'),
        ('Software Development', 'software_development')
    )

    card_category = models.CharField(
        max_length=50,
        help_text="The category of resources that the card relates to. It is used by the templating engine to sort the card.",
        verbose_name="Card Application Category",
        choices=resource_categories)

    # Changing Model MetaData:
    class Meta:
        # Plural Name in the Admin dashboard:
        verbose_name_plural = "Resources Index Cards"

    def generate_article_index_href(self):
        """The method manipulates the card_category model field to generate an
        the href
        """
        pass

    # __dunder methods:
    def __str__(self):
        return self.card_title

class Article(models.Model):
    """The data model that represents article posts in the 'education_resources' app.

    The Article model represents a single article post stored in the database. This is
    model that is queried to generate a list of articles in the 'articles_index.html'
    template. A single article can also be displayed in it's entirety based on the
    route probvided. A rendering of the whole article is largely done using the
    django plugin MarkdownX as the entire body of the article is written in markdown
    to allow for formatting and the embedding of images.

    An article should contain the following components:
    * A Title
    * An Author
    * A 'last updated' date value
    * A 'posted on' date value
    * Actual textual content (written in markdown)
    * The broader category the content of the article fits under. This is a ForeignKey
        that connects to an instance of the 'Resources_Index_Card' model as this
        is the most efficient means of assigning a category to an Article.

    These components make up the majority of the Model's fields however there
    are several other fields that have to do with an articles metadata that is
    used for searching and filtering on the backend:

    * Slug ID
    * A list of categories that the content of the article fits into.

    Reference:
        * https://www.existenceundefined.com/blog/programming/1/how-to-use-django-markdownx-for-your-blog
        * https://djangocentral.com/building-a-blog-application-with-django/
        * https://www.imzjy.com/blog/2018-05-20-render-the-markdown-in-django

    Attributes:

        title (models.CharField): The title string of the Article.

        author (models.ForeignKey): The ForeignKey connecting the Article to
            a User.

        last_updated (models.DateTimeField): The date value that auto updates every
            time the model is changed.

        created_date (models.DateTimeField): The date that the instance of the model
            was created.

        content (MarkdownxField): The Markdown text field representing the main
            content of the Article.

        main_category (models.ForeignKey): A ForeignKey connection to the 'Resources_Index_Card'
            data model. This is used to describe the main category the Article falls
            under by associating it with an instance of a Resources Index Card.

        slug (models.SlugField): The field that is used to identify a unique Article
            instance. This is used for URL generation and searching for the Article.

        categories (models.CharField): A seralized list of categories that are
            associated with the Article. This is a metadata field and is used for
            backend config and search.

    """
    # Declaring Displayed Article Fields:
    title = models.CharField(
        max_length = 200, unique=True,
        help_text = "The Title of the Article",
        verbose_name = "Article Title")
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "article_posts",
        verbose_name = 'Author')
    last_updated = models.DateTimeField(
        auto_now = True,
        help_text = "The last time the model has been updated/changed.",
        verbose_name = "Last Updated",
        editable=False)
    created_date = models.DateTimeField(
        auto_now_add = True,
        help_text = "The date when the article was posted.",
        verbose_name = "Date Posted",
        editable=False)
    content = MarkdownxField()
    main_category = models.ForeignKey(
        Resources_Index_Card,
        on_delete = models.CASCADE,
        help_text = "The associated Article Index Card model instance.",
        verbose_name = "Associated Article Index Card")

    # Declaring Article MetaData fields:
    slug = models.SlugField(
        max_length = 200,
        unique = True,
        blank = True)
    categories = models.CharField(
        max_length = 255,
        null = True,
        help_text = "A seralized list of categories that the article belongs to.",
        verbose_name = "MetaData Article Categories")


    # Describing MetaData for the Article model:
    class Meta:
        ordering = ["-created_date"]

    def save(self, *args, **kwargs):
        """
        Method overwrites the default Model save method in order to generate a
        slug value.

        This method is called ever time a new Article instance is saved, it
        takes in the title field for said instance and slugifys it, and saves
        the resulting output in the slug field. This means that a slug field is
        auto-generated every time an Article instance is created.

        Reference:
            * https://books.agiliq.com/projects/django-orm-cookbook/en/latest/slugfield.html

        Args:
            *args (*args): Boilerplate arguments for the default 'save' method.

            **kwargs (*kwargs): Boilerplate kew-word arguments for the default
                'save' method.
        """

        # Setting the slug value based on the title field:
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def serialized_categories_names(self):
        """Method that splits the serialized string of categories into
        a list of individual categories names.

        Multiple category strings are used in the Article model. As such
        they are stored as a single CharField in the database in serialized fashion
        with each category being seperated by a colon. Eg: 'category_a:category_b:category_c'.

        The method performs the .split(':') operation on the single string and
        returns a list of all categories to be used.

        Returns:
            list: The list of individual category strings generated by the
                split operation.

        """
        return self.categories.split(':')

    def content_markdown(self):
        """A Method that formats the markdown into HTML to be displayed in the
        front-end using the python markdown package.

        Returns:
             markdown.markdown: The markdown file rendered into HTML.
        """
        return markdown.markdown(self.content)

    def content_summary(self):
        """A method that returns a small sub-section of the content field.

        The method returns a markdown-rendered-to-HTML parameter. It performs
        the same function of the 'content_markdown()' method however it only
        renders the first 300 characters of the Atricle content field. This method
        is used to generate a summary of the article's context on the front-end.

        Returns:
            markdown.markdown: The first 300 characters of the content markdown file
                rendered into HTML.

        """
        return markdown.markdown(self.content[:300] + ".....")

    # __Dunder methods:
    def __str__(self):
        return self.title
