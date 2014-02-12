![Logo](logo.png)

The Open Supporter Data Interface (OSDI) effort seeks to define an API and data structures for interoperability among products in the **progressive** cause-based, campaign and non-profit marketplace. The existence of a common API will reduce customer costs related to moving data between different systems, lower integration costs and enhance the ability of innovators to create products for the marketplace.

OSDI membership is made up of progressive vendors and organizations as well as invited non-partisan and mainstream industry vendors.

More Information about OSDI can be found at the website [opensupporter.org](http://opensupporter.org)

[Download a one page PDF about the project](docs/osdi-one-pager.pdf)

[Experiment with our prototype server http://api.opensupporter.org](http://api.opensupporter.org)

[Play with our Canvasser example client application](http://canvasser.opensupporter.org)

Please give us feedback on our work. [Read the Review Guide](review_guide.md) to learn what kind of feedback we're looking for and how to provide it.

# Authors
* Tim Anderegg, New Organizing Institute (NOI)
* Topper Bowers, Amicus
* Beth Becker, Indigo Strategies
* Jeff Crigler, Catalist
* Josh Cohen, Washington United For Marriage (Editor)
* Michael Eskin, Blue State Digital
* Jascha Franklin-Hodge, Blue State Digital
* Tim Gutowski, Trilogy Interactive
* Chuck Hagenbuch, Blue State Digital
* Harlan Hill, Indigo Strategies
* Matt Klaber, NGP VAN
* Marc Love, Carbon Five
* Walter Ludwig, Indigo Strategies
* Drew Miller, NGP VAN
* Mark Paquette, TheDataBank
* Charles Parsons, Salsa Labs
* Rich Ranallo, Revolution Messaging
* Jason Rosenbaum, The Action Network
* Ben Stein, Mobile Commons
* Ray Suelzer, UFCW International Union
* Brian Vallelunga, Trilogy Interactive (Editor)
* Nathan Woodhull, ControlShift Labs
* Misha Zhurkin, Catalist

> This effort is currently in an exploratory phase to determine if consensus on a common API can be achieved.  The involvement of a person or company does not reflect a commitment to implement this API.

# Contact Info
Website: [http://opensupporter.org](http://opensupporter.org)

Email: [info@opensupporter.org](mailto:info@opensupporter.org)

# API Data Model

## Beta Stability Level
* [API Entry Point](aep.md)
* [People and Addresses](people.md)

## Experimental Stability Level
* [Lists](lists.md)
* [Survey Questions and Answers](questions.md)
* [Events](events.md)
* Donations
* [Canvassing Interactions](interactions.md)



# Basic Resource Access
## API Entry Point and linking
All access through OSDI starts at the API Entry Point (AEP).  The AEP is a resource that acts like a directory of the types of resources available on a server.  It also includes capability information like the maximum query pagesize.

Some servers may support some or all of the different resource collections.  For example, a peer to peer donation system might support Donations and People but not events.  In order to find out what resources are available and what URIs to use to access them, do a GET on the AEP URI.

Your service provider can tell you what the AEP URI is for your account.

For the purposes of example, assume your provider has given you an AEP URI of

[http://api.opensupporter.org/api/v1](http://api.opensupporter.org/api/v1)

> Note: you can explore the AEP with a user friendly interface by visiting our [prototype endpoint](http://api.opensupporter.org)

In order to determine the available resources on the server the client should perform an HTTP GET request to this URI.

Within the response will be a collection of links to the resource collections available on the server.


Request

	GET /api/v1 HTTP/1.1
	Host: api.opensupporter.org

Response

	200 OK
	Content-Type: application/json

	{
	  "motd": "Welcome to the ACME Action Platform OSDI API endpoint!!",
	  "_links": {
	    "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],  
	    "osdi:people": {
	      "href": "/api/v1/people",
	    },
		"osdi:people_lists": {
	      "href": "/api/v1/people_lists",
	    },
	    "odsi:questions": {
	      "href": "http://api.opensupporter.org/api/v1/questions",
	    },
	    "osdi:question_answers": {
	      "href": "http://api.opensupporter.org/api/v1/question_answers",
	    },
	    "self": {
	      "href": "/api/v1",
	    }
	  }
	}

Given the above example response, let's fetch the people collection on this server.
Notice the "_links" collection.  Find the object in the links collection with key "osdi:people".  That object has an attribute "href" which contains the URI to use to access the people collection.

> This is for example purpose only.  The official definition of the person schema is [People and Addresses](people.md)

Request

	GET /api/v1/people HTTP/1.1

Response

    {
		"total_records": 80,
			"total_pages": 16,
			"page" : 2,
			"_links": {
    			"next" : {
    				"href" : "http://api.opensupporter.org/api/v1/people?page=3&per_page=5"
				},
				"previous" : {
    				"href" : "http://api.opensupporter.org/api/v1/people?page=1&per_page=5"
    			}
    		},
			"people": [
				{
				"family_name": "Edwin",
					"given_name": "Labadie",
					"additional_name": "Marques",
					"identifiers": [
					"osdi:23"
				],
				"email_addresses": [
					{
						"address":"test-3@example.com",
						"primary": true,
						"address_type": "Personal"
					}
			],
			"phone_numbers": [
				{
					"primary": true,
					"number": 19876543210,
					"number_type": "Mobile",
					"sms_capable": true
				}
			],
			"gender": "Male",
			"gender_identity": "Male",
			"party_identification": "Democrat",
			"source": "sed",
			"ethnicity": "Caucasian",
			"profiles": [
				{
					"provider": "Twitter",
					"id": "Edwin_Labadie",
					"url": "http://twitter.com/Edwin_Labadie",
					"handle": "Edwin_Labadie"
				  }
			],
			"birth_date" : {
				"month" : 1,
				"day" : 1,
				"year" : 1970
			},
			"postal_addresses": [
				{
					"primary": true,
					"address_lines": [
						"935 Ed Lock"
					],
					"locality": "New Dudley",
					"region": "MN",
					"postal_code": "17678",
					"country": "RU",
					"address_type": "Home",
					"location" : {
						"longitude" : "40.1",
						"latitude" : "44.5",
						"accuracy": "Rooftop"
					},
					"status": "Verified"
				},
				{
					"address_lines": [
						"28160 Wiegand Divide"
					],
					"locality": "Lake Amarimouth",
					"region": "GA",
					"postal_code": "27585-7257",
					"country": "US",
					"address_type": "Work",
					"location" : {
						"longitude" : "40.1",
						"latitude" : "44.5",
						"accuracy": "Rooftop"
					},
					"status": "Verified",
					"primary": false
				}
			],
			"_links": {
				"curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
				"osdi:question_answers": {
					"href": "http://osdi-prototype.herokuapp.com/api/v1/people/23/question_answers"
				},
				"self": {
					"href": "http://osdi-prototype.herokuapp.com/api/v1/people/23"
				}
			}
		}, 
		
		.... other person records follow
	}


In the last example message, the server returns a list of people.  For brevity this document only shows the first one.  Within each person object, there is also a "_links" collection just like in the AEP.  This will show up in most objects in OSDI.  The links collection lets the client know what other resources and resource collections are associated with a given object.

In this example, the link shown is "osdi:question_answers".  The href attribute of the "osdi:question_answers" link contains the URI of the address collection *for this person*.

     "_links": {
          "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],         
          "osdi:question_answers": {
            "href": "http://api.opensupporter.org/api/v1/people/23/question_answers"
          }

A client can send a GET request to this URI to retrieve a list of question answers associated with this person.

Note that this pattern can be applied to other associated collections including but not limited to donations or question_answers.

## HAL

OSDI has embraced the [JSON+HAL spec](http://tools.ietf.org/html/draft-kelly-json-hal-05).  JSON+HAL specifies a simple way to embed linking into APIs.  The combination of linking and a specification allows generic clients to be written and, indeed, [many languages have HAL clients](http://stateless.co/hal_specification.html).  Linking itself makes it easier to both reason about and write clients for an API.

By default, server responses should expand first level instances unless otherwise specified.  For example, in a response for a collection of resources, those resources should be embedded.

### Curies

You may have noticed that most links are prefaced with a name space "osdi" and that in the _links section there is a key labeled "curies." The link section defines links to *relationships* between objects and curies define those relationships. You will find documentation on the particular relationship by using the templated curie link.  For example, given the following links section:

    "_links": {
      "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
      "self": {
        "href": "http://api.opensupporter.org/api/v1/question_answers/46"
      },
      "osdi:find": {
        "href": "http://api.opensupporter.org/api/v1/people?$filter={odata_query}",
        "templated": true
      }
    }
    
In order to fetch documentation on the question_answers relationship, I would visit the following url: "http://api.opensupporter.org/docs/v1/question_answers"

Any links not prefaced with a curie name space are defined here (http://www.iana.org/assignments/link-relations/link-relations.xml).

Vendors who add their own vendor-specific relationships must defined their own curie and preface their relationships with their own curie namespace.  For example,

    "_links": {
      "curies": [
        { "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true },
        { "name": "fb", "href": "http://facebook.com/docs/v1/{rel}", "templated": true }
      ],
      "self": {
        "href": "http://api.opensupporter.org/api/v1/question_answers/46"
      },
      "osdi:find": {
        "href": "http://api.opensupporter.org/api/v1/people?$filter={odata_query}",
        "templated": true
      },
      "fb:profile": {
          href: "http://facebook.com/profiles/1234"
      }
    }

HREFs within the links section may be templated.  That is denoted by the "templated": true attribute in the link object.  If the href is templated, then clients should follow the URI template spec (http://tools.ietf.org/html/rfc6570) to create the actual URI. At this time OSDI is only supporting simple variable substitution using the "{variable_name}" syntax.  For example, if I wanted to run a find on the collection above I would use the find link relation ("osdi:find").

I would then construct an odata_query and substitute the odata_query variable with my query string:

"http://api.opensupporter.org/api/v1/people?$filter={odata_query}", would become "http://api.opensupporter.org/api/v1/people?$filter=name eq 'bob'", for more information on odata queries see http://www.odata.org/documentation/odata-v2-documentation/uri-conventions/#45_Filter_System_Query_Option_filter.

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

To use the upsert feature, the $upsert query parameter is appended to the URI.  Its value is either true or false

> If the upsert parameter is not included, it defaults to TRUE.  The server will attempt a match to an existing resource first, but if if cannot find one, a new resource will be created.

	POST <addURI>?upsert=false HTTP/1.1
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

|Name			|Type		| Description
|-----------	|-----------|------------------------
|total_pages			|integer	|The number of pages applicable to this query
|total_records	|integer	|The total number of resources matching this query
|page			|integer	|The page number of this response


##### Prev/next
Collection responses may include additional links for navigation to previous and next pages

|Name		|Type		| Description
|-----------|-----------|------------------------
|next		|			|the link for the next page of results
|previous	|			|the link for the previous page of results

### Updating a Resource
Updating a resource instance is accomplished by the use of an HTTP PUT sent to the URI of a given resource.  Due to the complexity of full-resource updates involving read-only properties, out-of-date data, and the need to know all properties (which one may not), this specification focuses on the ability to make partial updates to resources.

To make an update to a resource, the client sends an HTTP PUT to the URI of a resource instance.  The body of the put contains a partial resource representation including the attributes to update.  Missing attributes are left unchanged on the Provider side.

Clients may set an attribute to nil by including the attribute using ‘nil’ for JSON.

> Updating Collections with PUT is not supported.

    PUT <editURI> HTTP/1.1
    Host: ...
    Accept: application/...
    Content-Type: application/...

    <serialization of request to update a resource>

    HTTP/1.1 200 OK
    Content-Type: application/...

    <serialization of updated resource>

    The HTTP response body shall contain the serialization of the updated resource

### Composite Requests (Updating or Creating with Embedded Resources)
In some situations, a client may wish to update or create a resource and include embedded resources in the same request.  For example, a client may wish to create or update a Person while including Address information.  The functionality to accomplish this is called a *Composite Request*

Composite Requests are only allowed with POST requests.

Support for Composite Requests is OPTIONAL.

Without Composite Requests, these scenarios would be accomplished with two separate requests. An initial request with a POST (for the create case) containing the parent resource (Person) information would be sent to the server.  Based on the response to this initial request, the client would learn the URI for the newly created resource.  A second POST request would be sent to that URI containing the representation of the child resource (Address)address to be added.  

To accomplish this in a single request, the client would use a Composite Request.  Composite requests are used with POST only.  A Composite request contains the representations of both the parent and child representations in a single request, according to the rules of HAL.  Child representations are contained within an _embedded JSON element.

Assuming the same example of updating or creating a Person and Address information in a composite request, the request body would contain the following information:

	{
	   "first_name": "Edwin",
       "last_name": "Labadie",
       "middle_name": "Marques",
       "email": "test-3@example.com",
       ... other attributes ...
       "_embedded": {
           "addresses": [ {
               "address1": "935 Ed Lock",
               "city": "New Dudley",
               "state": "MN",
               "postal_code": "17678",
               "country_code": "RU",
               "address_type": "Home",
               "lat": 44,
               "lng": 40,
               "accuracy": "Rooftop",
               "address_status": "Verified",
               "primary": true,
               ... other attributes ...
               },
               {
               "address1": "935 Ed Lock",
               "city": "New Dudley",
               "state": "MN",
               "postal_code": "17678",
               "country_code": "RU",
               "address_type": "Home",
               "lat": 44,
               "lng": 40,
               "accuracy": "Rooftop",
               "address_status": "Verified",
               ... other attributes ...
               } ]
        } 
    }              

### Composite Server Behavior
Composite requests that contain embedded representations may contain single embedded resources or resource collections (multiple instances of the same resource type).

Note that in the description below, the server shall order operations as specified.

##### Composite POST

When a composite request such as the example above is sent to a server with a POST method, first a new resource is created for the parent (Person). If that is successful, then new resources are created for the child or children (Address) resources.  If the upsert parameter is true, then the server may merge the transmitted resource representation with existing resources according to the rules of upsert.

##### Error Handling

If the attempt to update or create the parent resource fails, the server shall return the appropriate HTTP error code representing the failure.

If the attempt to update or create the child resource(s) fails, the server shall return the 409 Conflict HTTP response code.  Within the response body, the server shall include descriptive information on the nature of the child resource failure. This information is determined by best-effort.  Consistent with the definition of 409 Conflict, the assumption is that the user or client may need to examine the resulting resource state to determine the appropriate next steps.

##### Responses to Composite requests

If the composite server operations are successful, then a standard response containing the resource representations is returned.  It should contain the embedded resources as well.   
           
  
## Selecting Results
### Filtering Collections with OData

When retrieving collections, a client may request that the server filter the results according to a query.  OSDI makes use of a subset of the OData query language to accomplish this.  The filter string is the value of the 'filter' query parameter.

See [OData Filter Query] for more information. (http://www.odata.org/documentation/odata-v2-documentation/uri-conventions/#45_Filter_System_Query_Option_filter)

General information can be found at [odata.org](http://odata.org)
#### Conventions

* String literals are enclosed in single quotes, eg: 'Jon'
* Integers are not quoted, eg: 5
* The whole query string is not enclosed in any quotes

#### Operators

OSDI supports the following OData operators:

| Name  | Description | Example
|-------|-------------------------------|-------------------------------
| eq    | Exact match                   | first_name eq 'John'
| ne    | Not Equal exact match         | first_name ne 'John'
| gt    | Greater than                  | birthdate.month gt 1980
| ge    | Greater or equal than         | created gt '2013-11-17T18:27:35-05'
| lt    | Less than                     | birthdate.year lt 1980
| le    | Less or equal than            | created le '2013-11-17T18:27:35-05'
| or    | Logical OR                    | first_name eq 'John' or first_name eq 'Jon'
| and   | Logical AND                   | first_name eq 'John' and last_name eq 'Doe'
    
OSDI defines the following OPTIONAL extension operators:

| Name  | Description | Example
|-------|-------------------------------|------------------------------
| like  | Case insensitive match        | first_name like 'john'       # returns John or john
| re    | Matches a regular expression  | first_name regexp '/[Rr]ob/' # Returns robert, Robert, rob, roberto 

#### Functions

OSDI defines the following OPTIONAL extension functions:


| Name  | Description | Example
|-------|-------------|-----------------------------------------------
| near  | Returns entries near a location within a radius   | gender eq 'Female' and near('10011', '5 miles')

#### Examples

Find all males in a given ZIP code

    /api/v1/people?filter=gender eq 'Male' and address.postal_code eq '10011'
    
Find new signups on or since a date and time (Eastern Time)

    /api/v1/people?filter=created ge '2013-11-17T18:27:35-05'
    
    
### Pagination
The parameters $per_page and $page control pagination.

* $per_page specifies how many results to return per page
* $page specifies the starting page to start with.


### Expand / Mixins
In order to optimize access, the $expand query parameter can be used to expand collections within resources.  Normally when retrieving a resource instance, subordinate collections are returned as references.

When the $expand parameter is used, the collection corresponding to the parameter value shall be expanded to represent the collection of instances.

When this parameter is used in requests for Collections, the value applies to the resources enclosed in the collection rather than the collection itself.

Example

Assuming a resource of Person with a collection of addresses, $expand=addresses would cause the collection of instances of addresses to be returned rather than a reference.

## Common Attributes
All resources have a set of common attributes.  These are present, even if the table definitions do not explicitly list them.

### Common Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
|created_at	    |datetime   |The date and time the resource was created on the local system
|modified_at		|datetime	|The date and time the resource was last modified on the local system


## Notational Conventions

In this specification, when defining models, the following notational conventions are used.

|Convention	|Description
|:-----------:|--------------
|type[]     | A reference to a collection of resources of type 'type'
|	type*	| A reference to a single resource of type 'type'
|	string	| A string
|	datetime| A date and time representation.  In JSON this is a string.  The contents of this attribute shall be  ISO 8601 
| hash	| A complex attribute represented by a JSON hash

In the description of string types, sometimes the specification will list a set of acceptable values such as

| Name		| Type		| Description
|-----------|-----------|------------------
| gender	| string	| one of "Male", "Female", "Other" |

In these cases, the string value should conform to one of the choices unless specified otherwise

## Security

###	Encryption

Providers shall support secure HTTP connections using TLS. TLS 1.0, which shall be implemented, is specified in [RFC2246], and the TLS 1.1 and TLS 1.2 should be implemented as specified in [RFC4346] and [RFC5246], respectively.

Providers may support non-secure HTTP connections.

###	Authentication

Clients and Providers may use a variety of mechanisms to authenticate and authorize operations.  The specification does not currently require supporting a specific method.  However, there are many choices which can work with this specification.  

* Cookie Based Authentication
* HTTP Basic
* HTTP Digest
* Token Based Authentication
* OAuth and OAuth 2.0
* OpenID

Future versions of this specification may officially support one or more of these methods, or provide standard ways of implementing these methods, or may in other ways be more specific about security and authentication.
