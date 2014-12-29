## Endpoints and URL structures

OSDI does not specify specific endpoints and link structures for compliant systems to use. Rather, because OSDI is a HAL+JSON API, endpoints and structures are defined in the links section of each returned resource, starting with the API Entry Point link. 

HAL's link structure lets an API consumer move through API levels, resources, and collections by parsing and following links. While most systems will not change the value of their links often and obey RESTful design principles, the value of each link when that resource is retrieved is the only cannonical value, and it can change at any time.