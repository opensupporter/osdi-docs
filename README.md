
# Open Supporter Data Interface

The Open Supporter Data Interface (OSDI) is an effort to reduce customer costs related to moving data between different systems by defining a common API for products in the non-profit and campaign space.  We are a team of vendors and customers who are prioritizing customer cost reduction and interoperability.

The API will define interfaces including but not limited to resources representing people, donations, questions, tags, and events. The group will determine the order in which to define resource models and which version of the API to include them in.

[Read the full charter](charter.md)

[Read our scenarios document](scenarios/)

[Experiment with our prototype](http://osdi-prototype.herokuapp.com)

[Review Guide](review_guide.md)

# Authors
* Tim Anderegg, New Organizing Institute (NOI)
* Topper Bowers, Amicus
* Josh Cohen, Washington United For Marriage (Editor)
* Erik Lukoff, Change.org
* Charles Parsons, Salsa Labs

> This effort is currently in an exploratory phase to determine if consensus on a common API can be achieved.  The involvement of a person or company does not reflect a commitment to implement this API.

# API Data Model

* [API Entry Point](aep.md)
* [People and Addresses](people.md)
* Survey Questions and Answers
* Events
* Donations
* [Canvassing Interactions](interactions.md)



# Basic Resource Access
## API Entry Point and linking
All access through OSDI starts at the API Entry Point (AEP).  The AEP is a resource that acts like a directory of the types of resources available on a server.  It also includes capability information like the maximum query pagesize.

Some servers may support some or all of the different resource collections.  For example, a peer to peer donation system might support Donations and People but not events.  In order to find out what resources are available and what URIs to use to access them, do a GET on the AEP URI.

Your service provider can tell you what the AEP URI is for your account.

For the purposes of example, assume your provider has given you an AEP URI of

[http://osdi-prototype.herokuapp.com/api/v1](http://osdi-prototype.herokuapp.com/api/v1)

> Note: you can explore the AEP with a user friendly interface by visiting our [prototype endpoint](http://osdi-prototype.herokuapp.com)

In order to determine the available resources on the server the client should perform an HTTP GET request to this URI.

Within the response will be a collection of links to the resource collections available on the server.


Request

	GET /api/v1 HTTP/1.1
	Host: osdi-prototype.herokuapp.com

Response

	200 OK
	Content-Type: application/json

	{
	  "motd": "Welcome to the ACME Action Platform OSDI API endpoint!!",
	  "_links": {
	    "people": {
	      "href": "/api/v1/people",
	      "title": "The collection of people in the system"
	    },
	    "addresses": {
	      "href": "/api/v1/addresses",
	      "title": "The collection of addresses in the system"
	    },
	    "questions": {
	      "href": "http://osdi-prototype.herokuapp.com/api/v1/questions",
	      "title": "The collection of questions in the system"
	    },
	    "question_answers": {
	      "href": "http://osdi-prototype.herokuapp.com/api/v1/question_answers",
	      "title": "The collection of question answers in the system"
	    },
	    "self": {
	      "href": "/api/v1",
	      "title": "The root API Entry Point (Your are here)"
	    },
	    "docs": {
	      "href": "https://github.com/wufm/osdi-docs",
	      "title": "Documentation:",
	      "name": "Docs",
	      "index": "index"
	    }
	  }
	}

Given the above example response, let's fetch the people collection on this server. 
Notice the "_links" collection.  Find the object in the links collection with key "people".  That object has an attribute "href" which contains the URI to use to access the people collection.

Request

	GET /api/v1/people HTTP/1.1

Response
~~~~
{
  "count" : 5,
  "offset" : 0,
  "_embedded": {
    "people": [
      {
        "first_name": "Casey",
        "last_name": "Senger",
        "middle_initial": "W",
        "email": "test-1@example.com",
        "gender": "Male",
        "party": "Democrat",
        "source": "consequatur",
        "source_details": "Et iusto ea et blanditiis debitis aut at aspernatur.",
        "twitter_handle": "@Casey_Senger",
        "dwid": "qrbqa0eswt",
      ...other properties...
        "_links": {
              "addresses": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/1/addresses"
              }
	  ...
      ...
~~~~

In the last example message, the server returns a list of people.  For brevity this document only shows the first one.  Within each person object, there is also a "_links" collection just like in the AEP.  This will show up in most objects in OSDI.  The links collection lets the client know what other resources and resource collections are associated with a given object.

In this example, the link shown is "addresses".  The href attribute of the "addresses" link contains the URI of the address collection *for this person*.

A client can send a GET request to this URI to retrieve a list of addresses associated with this person.


### HAL
Resources contained in server responses shall be serialized with the Hypertext Application Language [HAL](http://stateless.co/hal_specification.html)
By default, server responses should expand first level instances.  For example, in a response for a collection of resources, those resources should be embedded.

## Common CRUD operations
### Creating a Resource
Creating a new resource involves adding a new item to a collection.  To create a new resource, an HTTP POST message is sent to the URI for a collection.

    POST <addURI> HTTP/1.1
    Host: ...
    Accept: application/...
    Content-Type: application/...

    <serialization of request to create a new resource>

    HTTP/1.1 201 Created
    Location: ...
    Content-Type: application/...

    <serialization of new resource>

#### Insert or Update (Upsert)
In some cases, the client doesn't know if a resource exists or not.  Instead of first having to query a resource to determine if it exists and then do an update via PUT, the client may use the upsert feature.

When used, the server will use a matching algorithm to determine if the input attributes match an existing record.

> The algorithm used by the server to perform matching is vendor-specific.  Contact your vendor for specifics.

To use the upsert feature, the $upsert query parameter is appended to the URI.

> If the upsert parameter is not included, it defaults to false.  The server will create a new resource

	POST <addURI>?upsert=true HTTP/1.1
    Host: ...
    Accept: application/...
    Content-Type: application/...

    <serialization of potential new resource>

If the resource does not exist, then a 201 response is returned

    HTTP/1.1 201 Created
    Location: ...
    Content-Type: application/...

    <serialization of new resource>

If the resource does already exist, then a 200 response is returned

 	HTTP/1.1 200 OK
    Location: ...
    Content-Type: application/...

    <serialization of existing resource>

### Retrieving a Resource
Retrieving a resource gets a representation of a resource instance or resource collection.  The retrieval is performed with an HTTP GET sent to the URI of the resource.

Request

    GET <ResourceURI> HTTP/1.1
    Host: ...
    Accept: application/...

Response

    HTTP/1.1 200 OK
    Content-Type: application/...

    <serialization of resource>

#### Collection Responses

When retrieving collections, the response representation will include some common attributes.

|Name		|Type		| Description
|-----------|-----------|------------------------
|count		|integer	|The number of resources returned in this response
|offset		|integer	|The offset of the first resource in the server collection

### Updating a Resource
Updating a resource instance is accomplished by the use of an HTTP PUT sent to the URI of a given resource.  Due to the complexity of full-resource updates involving read-only properties, out-of-date data, and the need to know all properties (which one may not), this specification focuses on the ability to make partial updates to resources.

To make an update to a resource, the client sends an HTTP PUT to the URI of a resource instance.  The body of the put contains a partial resource representation including the attributes to update.  Missing attributes are left unchanged on the Provider side.

Clients may set an attribute to nil by including the attribute using ‘nil’ for JSON.

Updating Collections with PUT is not supported.

    PUT <editURI> HTTP/1.1
    Host: ...
    Accept: application/...
    Content-Type: application/...

    <serialization of request to update a resource>

    HTTP/1.1 200 OK
    Content-Type: application/...

    <serialization of updated resource>

    The HTTP response body shall contain the serialization of the updated resource

## Selecting Results
### Filtering Collections
When retrieving representations of a collection, clients may include filters expressed as query parameters.  The $filter query parameter is used for this purpose.  The $filter parameter value shall contain an expression using the following operators:

        '<', '<=', '=', '>=', ">', '!=' : Integer and date value/attribute
        '=', '!='                       : String value/attribute

Example:
Assuming a resource of ‘Person’ which has an attribute named ‘firstName’, the following filter would return resources with first name of ‘Jon’

        $filter=first_name=’Jon’


### Pagination
The parameters $limit and $offset control pagination.

* $limit specifies how many results to return
* $offset specifies the starting point or offset to start with.


### Expand / Mixins
In order to optimize access, the $expand query parameter can be used to expand collections within resources.  Normally when retrieving a resource instance, subordinate collections are returned as references.

When the $expand parameter is used, the collection corresponding to the parameter value shall be expanded to represent the collection of instances.

When this parameter is used in requests for Collections, the value applies to the resources enclosed in the collection rather than the collection itself.

Example

Assuming a resource of Person with a collection of addresses, $expand=addresses would cause the collection of instances of addresses to be returned rather than a reference.

## Notational Conventions

In this specification, when defining models, the following notational conventions are used.

|Convention	|Description
|:-----------:|--------------
|type[]     | A reference to a collection of resources of type 'type'
|	type*	| A reference to a single resource of type 'type'
|	string	| A string
|	datetime| A date and time representation.  In JSON this is a string.  The contents of this attribute shall be  ISO 8601 

In the description of string types, sometimes the specification will list a set of acceptable values such as

| Name		| Type		| Description
|-----------|-----------|------------------
| gender	| string	| one of "Male", "Female", "Other" |

In these cases, the string value should conform to one of the choices unless specified otherwise