---
layout: default
title: "Tag"
---
# Tag
This document defines the Tag resource.

Tags represent categories of data that are associated with People resources. For example, an adminisrator might have a tag for volunteers. Each person who has signed up to volunteer would have the volunteer tag associated with them via a Tagging resource.

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Tag Fields](#tag-fields)  
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Tag resources (GET)](#scenario-retrieving-a-collection-of-tag-resources-get)
    * [Scenario: Retrieving an individual Tag resource (GET)](#scenario-scenario-retrieving-an-individual-tag-resource-get)
    * [Scenario: Creating a new tag (POST)](#scenario-creating-a-new-tag-post)
    * [Scenario: Modifying a tag (PUT)](#scenario-modifying-a-tag-put)
    * [Scenario: Deleting a tag (DELETE)](#scenario-deleting-a-tag-delete)

{% include endpoints_and_url_structures.md %}

## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


# Tag Fields

A list of fields specific to the Tag resource.

|Name   |Type   |Description
|---    |---    |---
|origin_system		|string     |A human readable identifier of the system where this form was created. (ex: "OSDI System")
|name				|string		|The name of the tag. Intended for administrative display rather than a public title, though may be shown to a user.
|description		|string		|A description of the tag, usually displayed publicly. May contain text and/or HTML.


_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Form*](forms.html)	|A self-referential link to the tag.
|creator		|[Person*](people.html)  		|A link to a single Person resource representing the creator of the tag.
|modified_by	|[Person* ](people.html) 		|A link to a Person resource representing the last editor of this tag.
|taggings	|[Taggings[]*](taggings.html)	|A link to the collection of Tagging resources for this tag.

_[Back to top...](#)_

## Related Resources

* [Tagging](tagging.md)
* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Tag resources (GET)

Tag resources are sometimes presented as collections of tags. For example, calling the tags endpoint will return a collection of all the tags stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/tags/

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
            "href": "https://osdi-sample-system.org/api/v1/tags?page=2"
        },
        "osdi:tags": [
            {
                "href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/tags/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/tags"
        }
    },
    "_embedded": {
        "osdi:tags": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "Volunteers",
                "description": "All activists who have signed up to volunteer.",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:taggings": {
                        "href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
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
                "name": "Donors",
                "description": "Any activist who has donated money.",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/tags/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:taggings": {
                        "href": "https://osdi-sample-system.org/api/v1/tags/1efc3644-af25-4253-90b8-a0baf12dbd1e/taggings"
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

### Scenario: Scenario: Retrieving an individual Tag resource (GET)

Calling an individual Tag resource will return the resource directly, along with all associated fields and appropriate links to additional information about the tag.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/tags/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
    "name": "Volunteers",
    "description": "All activists who have signed up to volunteer.",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
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


### Scenario: Creating a new tag (POST)

Posting to the tag collection endpoint will allow you to create a new tag. The response is the new tag that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/tags/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "name": "Volunteers",
    "origin_system": "OpenSupporter"
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
    "name": "Volunteers",
    "origin_system": "OpenSupporter",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a tag (PUT)

You can update a tag by calling a PUT operation on that tag's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "name": "2014 Volunteers",
    "description": "Volunteers from 2014"
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
    "name": "2014 Volunteers",
    "description": "Volunteers from 2014",
    "origin_system": "OpenSupporter",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a tag (DELETE)

You may delete a tag by calling the DELETE command on the tag's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/tags/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This tag was successfully deleted."
}
```

_[Back to top...](#)_