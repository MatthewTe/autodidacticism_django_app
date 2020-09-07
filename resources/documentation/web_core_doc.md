# The Web Core
The `web_core` application contains the routes and logic for both the main landing page, as well as the project index page. `web_core` is meant to serve as the 'core' of the site, with all other applications serving as modules that add functionality around `web_core`. The reason that the project index page is also contained within `web_core` is due to the intended structure of the entire project:

![IMAGE NOT FOUND](https://github.com/MatthewTe/autodidacticism_django_app/blob/master/resources/images/Django%20Application%20Diagram.png)

The poorly designed diagram shows how the logic and views for each of the apps is self contained, except for the `Applications`. The index page that lists the hosted applications is contained within the `web_core` app, whereas each of the actual hosted applications are contained within their own Django Apps which the `web_core` hosted index page just routes to.

The other two main functions of the Django project `education_resources` and `data_api` all contain their own internal routes, index pages and logic in traditional Django fashion.

## Web Core Routes:

### `index`
The index route is the homepage of the site. As this homepage is fairly basic the view just renders a static html file. There is no additional logic to the `index` view.

### `applications_index`
This is the page that lists the applications available on the site. Each application is displayed on the front-end as a bootstrap card, as part of a card deck with two columns. The applications are sorted by category on the index page and they are **dynamically generated**. Data for each application card is stored in the back-end through the web_core orm model `Applications_Index_Cards`. When the `applications_index` view is called the database is queried for all Application Index Cards. The resulting QuerySet is then passed into the `applications_index.html` template where it is iterated over and used to build bootstrap cards via logic in the templating engine.

**Example of dynamically generating BootStrap Cards in the `Web Applications` Section of the Applications Index Page:
```
{% comment %}
Itterating through the list of web framework application cards and dynamically generating each card from database:
{% endcomment %}
{% for card in application_cards %}

  {% if card.card_category == 'web_applications' %}
  <div class="col mb-4">
    <div class="card bg-dark">
      <div class="card-header">
        {% for icon_img in card.serialized_icon_names %}
          {# Building the icon url using |add: filter: #}
          {% with "web_core/images/icons/"|add:icon_img as icon_img_url %}
          <img id="card_icon" src="{% static icon_img_url %}" alt="">
          {% endwith %}
        {% endfor %}
      </div>
      {# Building the image url using |add: filter: #}
      {% with "web_core/images/"|add:card.card_image as main_card_img %}
      <img class="card-img-top" src="{% static main_card_img %}" alt="">
      {% endwith %}
      <div class="card-body">
        <h3 class=card-title>{{ card.card_title }}</h3>
        <hr style="border-color: black;">
        <p class="card-text text-justify">{{card.card_description}}</p>
      </div>
      <div class="btn-group" role="group" aria-label="Basic example">
        {# Building both button icon image urls using |add: filter: #}
        {% with "web_core/images/icons/"|add:card.button_a_icon as button_a_icon_url %}
        <a class="btn btn-info btn-outline-dark" href="{{ card.button_a_href }}">
          {{ card.button_a_text }} <img id='card_icon' src="{% static button_a_icon_url %}" alt="">
        </a>
        {% endwith %}
        {% with "web_core/images/icons/"|add:card.button_b_icon as button_b_icon_url %}
        <a class="btn btn-info btn-outline-dark" href="{{ card.button_b_href }}">
          {{ card.button_b_text }} <img id='card_icon' src="{% static button_b_icon_url %}" alt="">
        </a>
        {% endwith %}
      </div>
    </div>
  </div>
  {% endif %}
{% endfor %}
```
