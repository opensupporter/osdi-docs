---
layout: default
title: "Tagging"
---

# Tagging

This document defines the Tagging resource. 

Taggings represent a resource's association with a particular tag. Taggings have fields to describe them such as when the tagging was created and what type of resource it represents and typically are linked to the resource itself.

As an example, a customer might have a tag for volunteers.  Each Person who has signed up to volunteer would have the volunteer tag associated.  Tags are associated to a resource via a Tagging resource.

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Tagging Fields](#tagging-fields)  
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Tagging resources (GET)](#scenario-retrieving-a-collection-of-tagging-resources-get)
    * [Scenario: Retrieving an individual Tagging resource (GET)](#scenario-scenario-retrieving-an-individual-tagging-resource-get)
    * [Scenario: Creating a new tagging (POST)](#scenario-creating-a-new-tagging-post)
    * [Scenario: Modifying a tagging (PUT)](#scenario-modifying-a-tagging-put)
    * [Scenario: Deleting a tagging (DELETE)](#scenario-deleting-a-tagging-delete)
    
{% include endpoints_and_url_structures.md %}

The link relation label for a Tagging resource is ```osdi:tagging``` for a single Tagging resource or ```osdi:taggings``` for a collection of Tagging resources.

_[Back to top...](#)_

## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_

### Tagging Fields
A list of fields specific to the Tagging resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this tagging was created. (ex: "OSDI System")
|item_type		|string			|A property representing the type of resource this tagging links to. (ex: "osdi:person")

_[Back to top...](#)_

### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Tagging*](taggings.html)	|A self-referential link to the tagging.
|[resouce-name]			|[Resource*]		|A link to a single resource of the type indicated in the item_type field, representing the resource linked to the tagging.
|tag		|[Tag*](tags.html)  		|A link to a Tag resource representing the tag on which this tagging was created.

_[Back to top...](#)_

## Related Resources

* [Tag](tags.html)

_[Back to top...](#)_

# Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Tagging resources (GET)

Tagging resources are sometimes presented as collections of taggings. For example, calling the taggings endpoint on a particular tag will return a collection of all the taggings in that tag.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings

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
            "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings?page=2"
        },
        "osdi:taggings": [
            {
                "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings"
        }
    },
    "_embedded": {
        "osdi:taggings": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "item_type": "osdi:person",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:tag": {
                        "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29"
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
                "item_type": "osdi:event",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:tag": {
                        "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29"
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

### Scenario: Scenario: Retrieving an individual Tagging resource (GET)

Calling an individual Tagging resource will return the resource directly, along with all associated fields and appropriate links to additional information about the tagging.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

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
    "item_type": "osdi:person",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:tag": {
            "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new tagging (POST)

Posting to the taggings collection endpoint and including a link to an existing resource will allow you to create a new tagging associated with that tag and other resource. The response is the new tagging that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "item_type": "osdi:person",
    "_links" : {
        "osdi:person" : { 
            "href" : "https://actionnetwork.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f" 
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
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
        "foreign_system:1"
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "item_type": "osdi:person",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:tag": {
            "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://actionnetwork.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a tagging (PUT)

You can update an tagging by calling a PUT operation on that tagging's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/

Header:
OSDI-API-Token:[your api key here]

{
    "item_type": "osdi:event",
    "_links" : {
        "osdi:event" : { 
            "href" : "https://actionnetwork.org/api/v1/events/65345d7d-cd24-466a-a698-4a7686ef684f" 
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
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
        "foreign_system:1"
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T22:04:31Z",
    "item_type": "osdi:event",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:tag": {
            "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:events": {
            "href": "https://actionnetwork.org/api/v1/events/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a tagging (DELETE)

You may delete a tagging by calling the DELETE command on the taggin's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This tagging was successfully deleted."
}
```

_[Back to top...](#)_