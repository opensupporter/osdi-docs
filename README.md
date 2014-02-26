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

## Overview
OSDI used a combination of approaches to provide flexible reading of data, simple operations for simple scenarios, and general purpose CRUD access.

OSDI Compliant endpoints achieve this through the following capabilities

### RESTful Reading of Data (rest-read)
Reading of data, or querying resources, is done via traditional REST and Hypermedia practices.  OSDI uses HAL for hypermedia and OData query language to give a rich and flexible way to express queries

### Actions (actions)
OSDI also allows a client to perform actions, sometimes known as scenarios or methods, when the scenario is 'action oriented' vs 'data oriented' such as singing up a supporter, recording a donation, or rsvping for an event.

Certain common actions have been specifically defined to include any needed semantics to allow a client to perform an action in a single HTTP request/response.

### Direct Data Updates (rest-write)
There will always be an unbounded set of scenarios such that defining specific actions for each would be impractical.  For scenarios outside Actions, OSDI provides direct RESTful data access.  By using the common RESTful operations, along with hypermedia, virtually any scenario can be accomplished.

## API Entry Point and linking

### Overview
All access through OSDI starts at the API Entry Point (AEP).  The AEP is a resource that acts like a directory of the types of resources available on a server.  It also includes capability information like the maximum query pagesize.

Your service provider can tell you what the AEP URI is for your account.

For the purposes of example, assume your provider has given you an AEP URI of

[http://api.opensupporter.org/api/v1](http://api.opensupporter.org/api/v1)

> Note: you can explore the AEP with a user friendly interface by visiting our [prototype endpoint](http://api.opensupporter.org)

### Available Collections 
Some servers may support some or all of the different resource collections.  For example, a peer to peer donation system might support Donations and People but not events.  In order to find out what resources are available and what URIs to use to access them, do a GET on the AEP URI.


In order to determine the available resources on the server the client should perform an HTTP GET request to this URI.

Within the response will be a collection of links to the resource collections available on the server.

### Capabilities
Implementations of OSDI may differ in support of certain semantic capabilities.  Implementations may also define extensions to the OSDI specification.  A client may determine which capabilities are supported on a server by examining the "capabilities" hash inside of the AEP.

Some capabilities may be advertised merely by the presence of a boolean key, others may have complex hash structures indicating capability specific parameters.

### Example

Request

	GET /api/v1 HTTP/1.1
	Host: api.opensupporter.org

Response

	200 OK
	Content-Type: application/json

	{
	  "motd": "Welcome to the ACME Action Platform OSDI API endpoint!!",
	  "capabilities" : {
		"osdi:rest-read" : true,
		"osdi:actions" : true,
		"osdi:rest-write" : true,
		"acme:defeat_opponent": {								"modes" : [
				"landslide", "nailbiter"
			]
		},
	

	  "_links": {
	    "curies": [
			{"name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true },
			{"name": "acme", "href": "http://acme.foo/"}
		],  
	    "osdi:people": {
	      "href": "/api/v1/people",
	    },
		"osdi:people_lists": {
	      "href": "/api/v1/people_lists",
	    },
	    "osdi:addresses": {
	      "href": "/api/v1/addresses",
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


## Reading Data
Given the above example AEP response, let's fetch the people collection on this server.
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
    	  "_embedded": {
    	    "people": [
             {
                "first_name": "Edwin",
                "last_name": "Labadie",
                "middle_name": "Marques",
                "email": "test-3@example.com",
                "gender": "Male",
                "gender_identity": "Transgender Male",
                "party": "Democrat",
                "source": "sed",
                "source_details": "Delectus rerum autem mollitia sit asperiores odit hic cum.",
                "twitter_handle": "@Edwin_Labadie",
                "guid": "c1d9c510-b562-0130-dc7c-168c51e904de",
                "_embedded": {
                  "primary_address": {
                    "address1": "935 Ed Lock",
                    "city": "New Dudley",
                    "state": "MN",
                    "postal_code": "17678",
                    "country_code": "RU",
                    "address_type": "Home",
                    "location" : {
             		   "longitude" : "40.1",
             		   "latitude" : "44.5"4,
             		   "accuracy": "Rooftop"
             		 },
                    "address_status": "Verified",
                    "primary": true,
                    "_links": {
                      "self": {
                        "href": "http://api.opensupporter.org/api/v1/addresses/46"
                      },
                      "person": {
                        "href": "http://api.opensupporter.org/api/v1/people/23"
                      }
                    }
                  },
                  "addresses": [
                    {
                      "address1": "28160 Wiegand Divide",
                      "city": "Lake Amarimouth",
                      "state": "GA",
                      "postal_code": "27585-7257",
                      "country_code": "US",
                      "address_type": "Work",
                      "location" : {
             		      "longitude" : "40.1",
             		      "latitude" : "44.5"4,
             		      "accuracy": "Rooftop"
             		   },
                      "address_status": "Verified",
                      "primary": false,
                      "_links": {
                        "self": {
                          "href": "http://api.opensupporter.org/api/v1/addresses/45"
                        },
                        "person": {
                          "href": "http://api.opensupporter.org/api/v1/people/23"
                        }
                      }
                    },
                    {
                      "address1": "935 Ed Lock",
                      "city": "New Dudley",
                      "state": "MN",
                      "postal_code": "17678",
                      "country_code": "RU",
                      "address_type": "Home",
                      "location" : {
             		      "longitude" : "40.1",
             		      "latitude" : "44.5"4,
             		      "accuracy": "Rooftop"
             		   },
                      "address_status": "Verified",
                      "primary": true,
                      "_links": {
                        "self": {
                          "href": "http://api.opensupporter.org/api/v1/addresses/46"
                        },
                        "person": {
                          "href": "http://api.opensupporter.org/api/v1/people/23"
                        }
                      }
                    }
                  ]
                },
                "_links": {
                  "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
                  "osdi:addresses": {
                    "href": "http://api.opensupporter.org/api/v1/people/23/addresses"
                  },
                  "osdi:question_answers": {
                    "href": "http://api.opensupporter.org/api/v1/people/23/question_answers"
                  },
                  "self": {
                    "href": "http://api.opensupporter.org/api/v1/people/23"
                  }
                }
              }
            .... other person records follow
           }
        }


In the last example message, the server returns a list of people.  For brevity this document only shows the first one.  Within each person object, there is also a "_links" collection just like in the AEP.  This will show up in most objects in OSDI.  The links collection lets the client know what other resources and resource collections are associated with a given object.

In this example, the link shown is "osdi:addresses".  The href attribute of the "osdi:addresses" link contains the URI of the address collection *for this person*.

     "_links": {
          "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],         
          "osdi:addresses": {
            "href": "http://api.opensupporter.org/api/v1/people/23/addresses"
          }

A client can send a GET request to this URI to retrieve a list of addresses associated with this person.


    GET /api/v1/people/23/addresses

    200 OK
    Content-Type: application/json

    {
      "total_pages": 1,
      "page": 1,
      "total_records": 2,
      "_embedded": {
        "addresses": [
          {
            "address1": "28160 Wiegand Divide",
            "city": "Lake Amarimouth",
            "state": "GA",
            "postal_code": "27585-7257",
            "country_code": "US",
            "address_type": "Work",
            "location" : {
               "longitude" : "40.1",
             	"latitude" : "44.5"4,
             	"accuracy": "Rooftop"
             },
            "address_status": "Verified",
            "primary": false,
            "_links": {
              "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
              "self": {
                "href": "http://api.opensupporter.org/api/v1/addresses/45"
              },
              "osdi:person": {
                "href": "http://api.opensupporter.org/api/v1/people/23"
              }
            }
          },
          {
            "address1": "935 Ed Lock",
            "city": "New Dudley",
            "state": "MN",
            "postal_code": "17678",
            "country_code": "RU",
            "address_type": "Home",
            "location" : {
             	"longitude" : "40.1",
             	"latitude" : "44.5"4,
             	"accuracy": "Rooftop"
             },
            "address_status": "Verified",
            "primary": true,
            "_links": {
              "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
              "self": {
                "href": "http://api.opensupporter.org/api/v1/addresses/46"
              },
              "osdi:person": {
                "href": "http://api.opensupporter.org/api/v1/people/23"
              }
            }
          }
        ]
      },
      "_links": {
        "self": {
          "href": "http://api.opensupporter.org/api/v1/addresses"
        }
      }
    }

Note that this pattern can be applied to other associated collections including but not limited to donations or question_answers.

## HAL

OSDI has embraced the [JSON+HAL spec](http://tools.ietf.org/html/draft-kelly-json-hal-05).  JSON+HAL specifies a simple way to embed linking into APIs.  The combination of linking and a specification allows generic clients to be written and, indeed, [many languages have HAL clients](http://stateless.co/hal_specification.html).  Linking itself makes it easier to both reason about and write clients for an API.

By default, server responses should expand first level instances unless otherwise specified.  For example, in a response for a collection of resources, those resources should be embedded.

### Curies

You may have noticed that most links are prefaced with a name space "osdi" and that in the _links section there is a key labeled "curies." The link section defines links to *relationships* between objects and curies define those relationships. You will find documentation on the particular relationship by using the templated curie link.  For example, given the following links section:

    "_links": {
      "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
      "self": {
        "href": "http://api.opensupporter.org/api/v1/addresses/46"
      },
      "osdi:people_lists": {
        "href": "http://api.opensupporter.org/api/v1/people_lists"
      },
      "osdi:find": {
        "href": "http://api.opensupporter.org/api/v1/people?$filter={odata_query}",
        "templated": true
      }
    }
    
In order to fetch documentation on the people_lists relationship, I would visit the following url: "http://api.opensupporter.org/docs/v1/people_lists"

Any links not prefaced with a curie name space are defined here (http://www.iana.org/assignments/link-relations/link-relations.xml).

Vendors who add their own vendor-specific relationships must defined their own curie and preface their relationships with their own curie namespace.  For example,

    "_links": {
      "curies": [
        { "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true },
        { "name": "fb", "href": "http://facebook.com/docs/v1/{rel}", "templated": true }
      ],
      "self": {
        "href": "http://api.opensupporter.org/api/v1/addresses/46"
      },
      "osdi:people_lists": {
        "href": "http://api.opensupporter.org/api/v1/people_lists"
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

## Actions and Creating Resources

In numerous cases, creating a resource associated with an action, like recording a Donation, or signing up for an Event, the end result is that multiple resources need to be created (or updated).

When recording a donation, both donor information (like name and address) and donation information (like amount and currency) are typically captured.

In OSDI, donation resources and person resources are associated by a link.  This provides the ability to link multiple donations to a person as well as navigate from a person to an associated collection of donations.

In order to make this simple for clients, a special Create representation is used when POSTing to a collection.  These representations contain attributes for both resources like donation and person.

The server will process this action and create both resources with an association between them.

## Retrieving and Updating Resources
When retrieving a resource via GET, or updating with PUT or PATCH a different representation is used.

When retrieving an individual resource, the representation contains the attributes of that resource.  Associated resources are listed in the "_links" section and optionally sent in the "_embedded" section as a convenience.

When updating that resource via PUT or PATCH, only the attributes of the specified resource are sent.  In order to update the associated resources, the client should locate the URI for that resource in the "_links" section.

## Changing Relationships

Sometimes it is necessary to change which subordinate resource is linked to a primary resource.
Assume that a donation was created.  However, due to a matching error, the donation was matched with the wrong user.  The client wishes to change the association to that it points to the correct Person resource.

In order to provide this functionality, when a resource is retrieved, the "_links" section of the representation may contain links to a setter operation such as `osdi:set_person`.

To change a relationship, a client should send a POST to the setter resource containing the representation of the link destination.  Assuming a setter of `osdi:set_person`, the client would POST a representation of Person.

## Examples

### DonationCreate

To create a donation, a client sends a POST request to the donations collection.  In the body of the POST, the `DonationCreate` representation is used.


````javascript
POST /api/v1/1828182/donations

{
	options: {
		match: "match_and_store" // default	
		post_processing: true,
		"acme:magic_decoding_needed" : true
	},
	person: {
		"given_name" : "Testy",
		"family_name" : "McTesterson"
		... other person attributes
	},
	"donation_date" : "2013-11-19T08:37:48-0600",
	"amount" : 50.00,
	"currency" : "USD"
	... other DonationCreate fields
}

````
### DonationCreate Server Behavior
When the server processes a `DonationCreate`, the following things happen
1. A Donation resource is created
2. A person resource is created or merged based on provided information
3. If transactional is supported, then a donation_transaction is created containing the exact data contained in the DonationCreate representation

Response
The server shall respond to a DonationCreate with a Donation representation

````javascript
{
	"donation_date" : "2013-11-19T08:37:48-0600",
	"amount" : 50.00,
	"currency" : "USD"
	... other Donation fields
	"_embedded" : { // should these be inlined or relational
		"osdi:person" {
			"given_name" : "Testy",
			"family_name" : "McTesterson",
			... other person attributes
		},
		"osdi:donation_transaction" : {
			"person" : {
				"given_name" : "Testy",
				"family_name" : "McTesterson",
				... other person attributes
		
	},
	"_links" : {
		"osdi:person" : {
			"href": "http://server/path/to/person"
		},
		"osdi:donation_transaction" : {	
			"href": "http://path/to/donation_transaction",
		},
		"osdi:set_person" : {
			"href": "http://path/to/donation/5/set_person"
		},

		... other links
	}
}
````

### Working with Donation Resources
Reading data

A client sends a GET on the donations collection or an individual donation record

Updating Data
A client sends a PUT or PATCH to an individual Donation resource

### Working with DonationTransaction Resources
By having a separate donation transaction resource, we can customize this at will or even cherry pick data from other resources.

If a system does not support transactional data, then there is no complexity to the models.  It just does not show up in _embedded or _linked

Reading data

A client sends a GET on the DonationTransaction collection or an individual donation record

Updating Data
A client sends a PUT or PATCH to an individual DonationTransaction resource

## Changing an association
Sometimes it is necessary to change which subordinate resource is linked to a primary resource.
Assume that the above donation was created.  However, due to a matching error, the donation was matched with the wrong user.  The correct user is determined to have identifier "acme:1836283"

To change the Donation to be associated with the correct user, a client sends a POST message to the URL in the href in the osdi:set_person relation.
The server shall respond with the correct person object

````javascript
POST /path/to/donation5/set_person

{
  "identifiers" : [
  "acme:1836283"
  ]
}

200 OK

{
  "given_name" : "John",
  "family_name" : "Doe",
  "identifiers" : [
    "acme:1836283",
    "vanid:372938298"
    ]
  ... other person attributes
}
````

###Event RSVP
In order to simplify event signups, OSDI provides the event_signup action.  The event_signup endpoint is event specific.  It is returned within a specific event's representation.  It is expected that the client has this information in advance of the action.

````javascript
POST /api/v1/event543_url/attendance

{
	"person": {
		"email_address" : "testy@example.com"
		"identifiers" : [ "voterlabs:1234" ]
	},
  "creator" : {
    "given_name" : "James",
    "family_name" : "O'Field-Organizer",
}
	"status" : "accepted",
	"comment" : "1 phone bank == 5.3 votes!"
}

201 Created
Content-Type: application/json

{
  "_embedded" : {
    "osdi:person" : {
		"given_name" : "Testy",
    "family_name" : "McTesterson"
		"identitifiers" : [ "voterlabs:1234", "acme:3516516" ]
	  }
  }
 	"status" : "accepted",
	"comment" : "1 phone bank == 5.3 votes!"
	// continuation of donation resource attributes
	
	"_links" : {
		"self" : { "href" : "http://link/to/this/new/donation"},
		"osdi:person" : { "href" : "http://link/to/associated/person"}
    "osdi:set_person" { "href" : "http://link/to/set/associated/person"},
	"osdi:set_creator" : {
		"href": "http://path/to/donation/5/set_creator"
		}
	}
}

````

## Writing Data (rest-write)
RESful writing, or updating of data is done via common RESTful (CRUD) operations
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
