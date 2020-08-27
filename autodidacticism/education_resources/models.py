from django.db import models

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

        button_a_href (models.CharField): The text representing the link that will be
            attached to the button.

        button_b_txt (models.CharField): The text of the second card button in the button
            group.

        button_b_icon (models.CharField): The CharField representing the name of the icon
            image to be attached to the button.

        button_b_href (models.CharField): The text representing the link that will be
            attached to the button.

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
        help_text="The name of the icon image to be inserted into the first button.",
        verbose_name="Button A Icon")
    button_a_href = models.CharField(
        max_length=225,
        help_text="The url that the first button is supposed to lead to.",
        verbose_name="Button A Href")

    # Button B Content:
    button_b_text = models.CharField(
        max_length=50,
        help_text='The main text content of the second button.',
        verbose_name="Button B Text")
    button_b_icon = models.CharField(
        max_length=50,
        help_text="The name of the icon image to be inserted into the second button.",
        verbose_name="Button B Icon")
    button_b_href = models.CharField(
        max_length=225,
        help_text="The url that the second button is supposed to lead to.",
        verbose_name="Button B Href")

    # Card MetaData:
    card_category = models.CharField(
        max_length=50,
        help_text="The category of resources that the card relates to. It is used by the templating engine to sort the card.",
        verbose_name="Card Application Category")
