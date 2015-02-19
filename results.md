---
layout: default
title: Result
---

# Result

This document defines the Result resource. 

Results represent a resource's membership in the results of a query. Results have fields to describe them such as when the result was created and what type of resource it represents and typically are linked to the resource itself.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Result Fields](#result-fields)  
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Result resources (GET)](#scenario-retrieving-a-collection-of-result-resources-get)
    * [Scenario: Retrieving an individual Result resource (GET)](#scenario-scenario-retrieving-an-individual-result-resource-get)
    * [Scenario: Creating a new result (POST)](#scenario-creating-a-new-result-post)
    * [Scenario: Modifying a result (PUT)](#scenario-modifying-a-result-put)
    * [Scenario: Deleting a result (DELETE)](#scenario-deleting-a-result-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Result resource is ```osdi:result``` for a single Result resource or ```osdi:results``` for a collection of Result resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Result Fields

A list of fields specific to the Result resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this result was created. (ex: "OSDI System")
|result_type		|string			|A read-only property representing the type of resource this result links to. (ex: "osdi:person")

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Result*](results.html)	|A self-referential link to the result.
|[resouce-name]			|[Resource*]		|A link to a single resource of the type indicated in the result_type field, representing the resource linked to the result.
|query		|[Query*](queries.html)  		|A link to a Query resource representing the query on which this result was created.

**Note:** Because results represent the actual results of a query in real time, resources that results link to will not reciprocally display a link back to a collection of results for that resource, as it typical with other similar resources such as signatures. This is done to protect system resources. For example, a person resource will not have a link to a collection of results associated with that person, as this would easily cause high server load as the system re-runs all queries to determine which queries that person matches at that moment.

_[Back to top...](#)_


## Related Resources

* [Query](queries.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Result resources (GET)

Result resources are sometimes presented as collections of results. For example, calling the results endpoint on a particular query will return a collection of all the results made on that query.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29/results

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
            "href": "https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29/results?page=2"
        },
        "osdi:results": [
            {
                "href": "https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29/results/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29/results/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29/results"
        }
    },
    "_embedded": {
        "osdi:results": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "result_type": "osdi:person",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29/results/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:query": {
                        "href": "https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
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
                "result_type": "osdi:event",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29/results/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:query": {
                        "href": "https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:event": {
                        "href": "https://osdi-sample-system.org/api/v1/events/adb951cb-51f9-420e-b7e6-de953195ec86"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Result resource (GET)

Calling an individual Result resource will return the resource directly, along with all associated fields and appropriate links to additional information about the result.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29/results/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

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
    "result_type": "osdi:person",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29/results/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:query": {
            "href": "https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new result (POST)

Because query results represent the end of a query calculation process performed by the server, creating results via the API is not supported. If you wish to hand-create lists of resources, use the [List](lists.html) resource instead.

_[Back to top...](#)_


### Scenario: Modifying a result (PUT)

You can update a result by calling a PUT operation on that result's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29/results/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
	    "foreign_system:2"
	]
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
        "foreign_system:1",
        "foreign_system:2"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "result_type": "osdi:person",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29/results/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:query": {
            "href": "https://osdi-sample-system.org/api/v1/queries/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a result (DELETE)

Because query results represent the end of a query calculation process performed by the server, deleting results via the API is not supported. If you wish to hand-create or delete lists of resources, use the [List](lists.html) resource instead.

_[Back to top...](#)_