---
layout: default
title: Wrapper
---

# Wrapper

This document defines the Wrapper resource. 

Wrapper resources represent a some type of standard wrapper around a Message resource. For example a mass email will have HTML that typically adds a standard header and footer to the email message, whereas SMS will have standard from lines and unsubscribe text that will be added, etc... Wrappers have fields to describe them such as HTML headers and footers. Wrappers can be linked by Messages to show which wrapper the message is using.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Wrapper Fields](#wrapper-fields)  
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Wrapper resources (GET)](#scenario-retrieving-a-collection-of-wrapper-resources-get)
    * [Scenario: Retrieving an individual Wrapper resource (GET)](#scenario-scenario-retrieving-an-individual-wrapper-resource-get)
    * [Scenario: Creating a new wrapper (POST)](#scenario-creating-a-new-wrapper-post)
    * [Scenario: Modifying a wrapper (PUT)](#scenario-modifying-a-wrapper-put)
    * [Scenario: Deleting an wrapper (DELETE)](#scenario-deleting-a-wrapper-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for an Wrapper resource is ```osdi:wrapper``` for a single Wrapper resource or ```osdi:wrappers``` for a collection of Wrapper resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Wrapper Fields

A list of fields specific to the Wrapper resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this wrapper was created. (ex: "OSDI System")
|name				|string		|The name of the wrapper. Intended for administrative display rather than a public title, though may be shown to a user.
|header				|string		|The header content of the wrapper. May contain HTML.
|footer				|string		|The footer content of the wrapper. May contain HTML.
|administrative_url		|string		|A URL string pointing to the wrapper's administrative page on the web.
|wrapper_type				|enum		|The type of wrapper. One of "email" or "sms".
|default			|boolean	|Whether this wrapper is the default wrapper for messages or not.

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Wrapper*](wrappers.html)	|A self-referential link to the wrapper.
|creator		|[Person*](people.html)  		|A link to a single Person resource representing the creator of the wrapper.
|modified_by	|[Person* ](people.html) 		|A link to a Person resource representing the last editor of this wrapper.

_[Back to top...](#)_


## Related Resources

* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Wrapper resources (GET)

Wrapper resources are sometimes presented as collections of wrappers. For example, calling the wrappers endpoint will return a collection of all the wrappers stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/wrappers/

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
            "href": "https://osdi-sample-system.org/api/v1/wrappers?page=2"
        },
        "osdi:wrappers": [
            {
                "href": "https://osdi-sample-system.org/api/v1/wrappers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/wrappers/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/wrappers"
        }
    },
    "_embedded": {
        "osdi:wrappers": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "GOTV email wrapper",
                "header": "<p>It's time to go vote!</p>",
                "footer": "<p>Sent by the campaign to elect Jane Doe.</p>",
                "administrative_url": "http://osdi-sample-system.org/wrappers/gotv/manage",
                "wrapper_type": "email",
                "default": true,
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/wrappers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
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
                "name": "GOTV SMS wrapper",
                "administrative_url": "http://osdi-sample-system.org/wrappers/gotv/manage",
                "wrapper_type": "sms",
                "default": true,
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/wrappers/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Wrapper resource (GET)

Calling an individual Wrapper resource will return the resource directly, along with all associated fields and appropriate links to additional information about the wrapper.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/wrappers/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
    "name": "GOTV email wrapper",
    "header": "<p>It's time to go vote!</p>",
    "footer": "<p>Sent by the campaign to elect Jane Doe.</p>",
    "administrative_url": "http://osdi-sample-system.org/wrappers/gotv/manage",
    "wrapper_type": "email",
    "default": true,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/wrappers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
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


### Scenario: Creating a new Wrapper (POST)

Posting to the wrappers collection endpoint will allow you to create a new wrapper. Optionally adding a link to a Person resource will set the creator. The response is the new wrapper that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/wrappers/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "name": "GOTV email wrapper",
    "header": "<p>It's time to go vote!</p>",
    "footer": "<p>Sent by the campaign to elect Jane Doe.</p>",
    "wrapper_type": "email",
    "default": true
}
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
    "name": "GOTV email wrapper",
    "header": "<p>It's time to go vote!</p>",
    "footer": "<p>Sent by the campaign to elect Jane Doe.</p>",
    "administrative_url": "http://osdi-sample-system.org/wrappers/gotv/manage",
    "wrapper_type": "email",
    "default": true,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/wrappers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
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


### Scenario: Modifying a wrapper (PUT)

You can update a wrapper by calling a PUT operation on that wrapper's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/wrappers/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "name": "GOTV wrapper version 2"
}

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
    "name": "GOTV wrapper version 2",
    "header": "<p>It's time to go vote!</p>",
    "footer": "<p>Sent by the campaign to elect Jane Doe.</p>",
    "administrative_url": "http://osdi-sample-system.org/wrappers/gotv/manage",
    "wrapper_type": "email",
    "default": true,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/wrappers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
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



### Scenario: Deleting a wrapper (DELETE)

You may delete a wrapper by calling the DELETE command on the wrapper's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/wrappers/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This wrapper was successfully deleted."
}
```

_[Back to top...](#)_