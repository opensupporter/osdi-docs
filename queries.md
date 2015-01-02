---
layout: default
title: Query
---

# Query

This document defines the Query resource. 

Queries represent the results of a process on the server to create a collection of resources that share characteristics. For example, a query can represent the result of a SQL targeting operation. Queries have results which represent the individual resources that are part of the query's resulting collection. 

A query must fit a set of criteria:

* Query results are nonarbitrary -- a resource's inclusion in the collection is based on attributes intrinsic to that resource, as opposed to having been put there by hand. For hand-created lists of resources, use the [List](lists.html) resource instead.
* Queries may only be dynamic -- a query will return the resources which match its criteria at the moment the Query resource is retrieved. To implement a static query, which contains the resources which matched its criteria at the time the query was created or saved, the [List](lists.html) resource should be used instead.
* Query targeting criteria may only be created, deleted and edited on the content provider's native system -- OSDI does not currently support an API-driven query, targeting, or SQL language. 
* Consequently, OSDI does not support CRUD operations on queries beyond updating metadata. Queries may only be created or deleted via the API provider's system.
* Queries are unique collections of resources -- a resource may match a query only once.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Query Fields](#query-fields)  
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Query resources (GET)](#scenario-retrieving-a-collection-of-query-resources-get)
    * [Scenario: Retrieving an individual Query resource (GET)](#scenario-scenario-retrieving-an-individual-query-resource-get)
    * [Scenario: Creating a new query (POST)](#scenario-creating-a-new-query-post)
    * [Scenario: Modifying a query (PUT)](#scenario-modifying-a-query-put)
    * [Scenario: Deleting a query (DELETE)](#scenario-deleting-a-query-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Form resource is ```osdi:query``` for a single Query resource or ```osdi:queries``` for a collection of Query resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Query Fields

A list of fields specific to the Query resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this query was created. (ex: "OSDI System")
|name				|string		|The name of the query. Intended for administrative display rather than a public title, though may be shown to a user.
|title				|string		|The title of the query. Intended for public display rather than administrative purposes.
|description		|string		|A description of the query, usually displayed publicly. May contain text and/or HTML.
|summary			|string		|A text-only single paragraph summarizing the query. Shown on listing pages that have more than titles, but not enough room for full description.
|browser_url		|string		|A URL string pointing to the publicly available query page on the web.
|total_results	|integer	|A read-only computed property representing the current count of the total number of results for the query.

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Query*](queries.html)	|A self-referential link to the query.
|creator		|[Person*](people.html)  		|A link to a single Person resource representing the creator of the query.
|modified_by	|[Person* ](people.html) 		|A link to a Person resource representing the last editor of this query.
|results	|[Results[]*](results.html)	|A link to the collection of Results resources for this query.

_[Back to top...](#)_


## Related Resources

* [Result](result.html)
* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Query resources (GET)

Query resources are sometimes presented as collections of queries. For example, calling the queries endpoint will return a collection of all the queries stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/queries/

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "total_pages": 10,
    "per_page": 25,
    "page": 1,
    "total_records": 250,
    "_links": {
        "next": {
            "href": "https://osdi-sample-system.org/api/v1/queries?page=2"
        },
        "osdi:queries": [
            {
                "href": "https://osdi-sample-system.org/api/v1/queries/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/queries/1efc3644-af25-4253-90b8-a0baf12dbd1e"
            },
            //(truncated for brevity)
        ],
        "curies": [
            {
                "name": "osdi",
                "href": "https://osdi-sample-system.org/docs/v1/{rel}",
                "templated": true
            }
        ],
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/queries"
        }
    },
    "_embedded": {
        "osdi:queries": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "Justice Petition Signers",
                "summary": "Petition signers on the December justice petition.",
                "browser_url": "http://osdi-sample-system.org/queries/justice-petition-signers",
                "total_results": 26497,
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/queries/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:results": {
                        "href": "https://osdi-sample-system.org/api/v1/queries/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/results"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    }
                }
            },
            {
                "identifiers": [
                    "osdi_sample_system:1efc3644-af25-4253-90b8-a0baf12dbd1e"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T20:44:13Z",
                "modified_date": "2014-03-20T20:44:13Z",
                "title": "1/2/15 email",
                "browser_url": "http://osdi-sample-system.org/queries/1215-email",
                "total_results": 108273,
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/queries/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:results": {
                        "href": "https://osdi-sample-system.org/api/v1/queries/1efc3644-af25-4253-90b8-a0baf12dbd1e/results"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Query resource (GET)

Calling an individual Query resource will return the resource directly, along with all associated fields and appropriate links to additional information about the query.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/queries/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "Justice Petition Signers",
    "summary": "Petition signers on the December justice petition.",
    "browser_url": "http://osdi-sample-system.org/queries/justice-petition-signers",
    "total_results": 26497,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/queries/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:results": {
            "href": "https://osdi-sample-system.org/api/v1/queries/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/results"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new query (POST)

Because OSDI does not currently support an API-driven query, targeting, or SQL language, creating queries via the API is also not supported.

_[Back to top...](#)_


### Scenario: Modifying a query (PUT)

You can update a query by calling a PUT operation on that query's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "name": "December Justice Petition Signers"
}

```

#### Response
```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
        "foreign_system:1"
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T22:04:31Z",
    "name": "December Justice Petition Signers",
    "summary": "Petition signers on the December justice petition.",
    "browser_url": "http://osdi-sample-system.org/queries/justice-petition-signers",
    "total_results": 26497,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/queries/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:results": {
            "href": "https://osdi-sample-system.org/api/v1/queries/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/results"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a query (DELETE)

Because OSDI does not currently support an API-driven query, targeting, or SQL language, deleting queries via the API is also not supported.

_[Back to top...](#)_