# Educational Resources
This Django App handles all of the educational content on the site. The App is tasked with providing a central repository for the educational resources that are made use of and providing a means of creating and hosting my own resources (articles, research papers, documentation) on various topics.

## Educational Resources Routes:

### `resources_index`
This is the index page for the list of educational resources. Much like the `applications_index` the resources index page displays each category as a Bootstrap Card in a card deck with two columns. These cards are again **Dynamically Generated.** The logic that is used to generate these index cards is the same logic that is used in the web_core index page. The data used to build the cards is represented in the database through the `education_resources` data model `Resources_Index_Card` orm model. 
