# Autodidacticism Django App
The source code for the Autodidacticism website written in python using the Django library. The Documentation assumes a base understanding of the Django framework and application structure and seeks to explain the core components of the Project and all of the interactions between Applications.

## Hosting
TODO: Add An example of how to host once hosting becomes possible.

## Applications
There are three main objectives that the Django project seeks to meet:
* The hosting of personal projects/applications
* Providing a central repository for the educational resources that I make use of and providing me a means of creating and hosting my own resources (articles, research papers, documentation) on various topics.
* Hosting Web Data APIs that serve data that is either collected by my web scraping application (see objective 1.) or other forms of data collection.

Based on these three functions, there are three main applications that form the core of the Django project:
* `web_core`
* `education_resources`
* `data_api`

### The Web Core
The `web_core` application contains the routes and logic for both the main landing page, as well as the project index page. `web_core` is meant to serve as the 'core' of the site, with all other applications serving as modules that add functionality around `web_core`. The reason that the project index page is also contained within `web_core` is due to the intended structure of the entire project:
![IMAGE NOT FOUND](https://github.com/MatthewTe/autodidacticism_django_app/blob/master/resources/Django%20Application%20Diagram.png)

The poorly designed diagram shows how the logic and views for each of the apps is self contained, except for the `Applications`. The index page that lists the hosted applications is contained within the `web_core` app, whereas each of the actual hosted applications are contained within their own Django Apps which the `web_core` hosted index page just routes to.

The other two main functions of the Django project `education_resources` and `data_api` all contain their own internal routes, index pages and logic in traditional Django fashion.
