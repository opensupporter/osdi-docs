---
layout: default
title: Canvassing Efforts
---

# Canvassing Effort

This page defines the Canvassing Effort resource.

Canvassing Efforts represent specific canvassing/phone banking events planned for a specific time period. The resource contains information about start and end time, people to be canvassed or called, and a [Script](scripts.html) that is used for the effort. 

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Script Fields](#effort-fields) 
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Canvassing Effort resources (GET)](#scenario-retrieving-a-collection-of-canvassing-effort-resources-get)
    * [Scenario: Retrieving an individual Canvassing Effort resource (GET)](#scenario-retrieving-an-individual-canvassing-effort-resource-get)
    * [Scenario: Creating a new Canvassing Effort (POST)](#scenario-creating-a-new-canvassing-effort-post)
    * [Scenario: Modifying a Canvassing Effort (PUT)](#scenario-modifying-a-canvassing-effort-put)
    * [Scenario: Deleting a Canvassing Effort (DELETE)](#scenario-deleting-a-canvassing-effort-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for an Canvassing Effort resource is ```osdi:canvassing_effort``` for a single Canvassing Effort resource or ```osdi:canvassing_efforts``` for a collection of Canvassing Effort resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_

### Canvassign Effort Fields

| Name          | Type                | Description
| -----------   | -----------         | --------------
|origin_system      |string     |A human readable identifier of the system where this effort was created. (ex: "OSDI System")
|name               |string     |The name of the Canvassing Effort. Intended for administrative display rather than a public title, though may be shown to a user.
|title              |string     |The title of the Canvassing Effort. Intended for public display rather than administrative purposes.
|description        |string     |A description of the Canvassing Effort, usually displayed publicly. May contain text and/or HTML.
|summary            |string     |A text-only single paragraph summarizing the effort. Shown on listing pages that have more than titles, but not enough room for full description.
|start_time        |string     |The start date and time for the Canvassing Effort.
|end_time        |string     |The end date and time for the Canvassing Effort.
|type           |string      |The type of the Canvassing Effort "in-person","phone banking",etc 

_[Back to top...](#)_

### Links

{% include links_intro.md %}

| Name          | Type       | Description
|-----------    |----------- |-----------
|self           |[Canvassing Effort*](canvassing_efforts.html)    |A self-referential link to the canvassing effort.
|creator        |[Person*](people.html)         |A link to a single Person resource representing the creator of the Canvassing Effort.
|modified_by    |[Person* ](people.html)        |A link to a Person resource representing the last editor of this Canvassing Effort.
|script  |[Script*](script.html) | A link to the script associated with the canvassing effort

_[Back to top...](#)_


## Related Resources

* [Person](people.html)
* [Script](scripts.html)
* [Canvass](canvasses.html)


_[Back to top...](#)_


## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Canvassing Effort resources (GET)

Canvassing Effort resources are sometimes presented as collections of canvassing efforts. For example, calling the canvassing_efforts endpoint will return a collection of all the canvassing efforts stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/canvassing_efforts/

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
            "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts?page=2"
        },
        "osdi:canvassing_efforts": [
            {
                "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts"
        }
    },
    "_embedded":
    {
        "osdi:canvassing_efforts": [
            {
                "identifiers": [
                    "osdi_sample_system:a91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bca",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "Effort 1",
                "title": "Team 1",
                "description": "Effort 1 for Team 1",
                "summary": "Effort 1 for Team 1",
                "start_time": "2016-02-19T8:00:00Z",
                "end_time": "2016-02-20T8:00:00Z",
                "type": "canvassing",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:script" : {
                            "href": "https://osdi-sample-system.org/api/v1/script/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ba3"
                    }
                }
            },
            {
                "identifiers": [
                    "osdi_sample_system:a91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bca",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "Effort 2",
                "title": "Team 1",
                "description": "Effort 2 for Team 1",
                "summary": "Effort 2 for Team 1",
                "start_time": "2016-02-19T8:00:00Z",
                "end_time": "2016-02-20T8:00:00Z",
                "type": "canvassing",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:script" : {
                            "href": "https://osdi-sample-system.org/api/v1/script/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ba3"
                    }
                }
            },   
            //truncated for brevity
        ]
    }
}
``` 

_[Back to top...](#)_       

### Scenario: Retrieving an individual Canvassing Effort resource (GET)

Calling an individual Canvassing Effort resource will return the resource directly.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/canvassing_efforts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa

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
        "osdi_sample_system:a91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bca",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "Effort 2",
    "title": "Team 1",
    "description": "Effort 2 for Team 1",
    "summary": "Effort 2 for Team 1",
    "start_time": "2016-02-19T8:00:00Z",
    "end_time": "2016-02-20T8:00:00Z",
    "type": "in-person",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:script" : {
                "href": "https://osdi-sample-system.org/api/v1/script/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ba3"
        }
    }
}
```


_[Back to top...](#)_


### Scenario: Creating a new Canvassing Effort (POST)

Posting to the effort collection endpoint will allow you to create a new effort. The response is the new effort that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/canvassing_efforts/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "name": "Effort 2",
    "title": "Team 1",
    "description": "Effort 2 for Team 1",
    "summary": "Effort 2 for Team 1",
    "start_time": "2016-02-19T8:00:00Z",
    "end_time": "2016-02-20T8:00:00Z",
    "type": "in-person",
    "_links": {
        "osdi:script": {
            "href": "https://osdi-sample-system.org/api/v1/script/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ba3"
        }
    }
}

```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate
{
    "identifiers": [
        "osdi_sample_system:a91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bca",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "Effort 2",
    "title": "Team 1",
    "description": "Effort 2 for Team 1",
    "summary": "Effort 2 for Team 1",
    "start_time": "2016-02-19T8:00:00Z",
    "end_time": "2016-02-20T8:00:00Z",
    "type": "in-person",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:script" : {
                "href": "https://osdi-sample-system.org/api/v1/script/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ba3"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a Canvassing Effort (PUT)

You can update an effort by calling a PUT operation on that effort's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/canvassing_efforts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa

Header:
OSDI-API-Token:[your api key here]

{
    "name": "Effort 2",
    "title": "Canvassing Effort 2"
}

```

#### Response
```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate
{
    "identifiers": [
        "osdi_sample_system:a91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bca",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "Effort 2",
    "title": "Team 1",
    "description": "Effort 2 for Team 1",
    "summary": "Effort 2 for Team 1",
    "start_time": "2016-02-19T8:00:00Z",
    "end_time": "2016-02-20T8:00:00Z",
    "type": "in-person",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:script" : {
                "href": "https://osdi-sample-system.org/api/v1/script/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ba3"
        }
    }
}
```


_[Back to top...](#)_


### Scenario: Deleting a Canvassing Effort (DELETE)

You may delete an effort by calling the DELETE command on the Canvassing Effort's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/canvassing_efforts/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This canvassing effort was successfully deleted."
}
```

_[Back to top...](#)_
