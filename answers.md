---
layout: default
title: Answer Resource
---

# Answer Resource

Answers are applied to a the Person resource and include a link to the cooresponding Question resource. 

As an example, a Question might ask Do you support John Doe For City Council?  An Answer would be a Persons response to the question. 

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Resource Fields](#resource-fields)
* [Helpers](#helpers)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of resources (GET)](#scenario-retrieving-a-collection-of-resources-get)
    * [Scenario: Retrieving an individual resource (GET)](#scenario-scenario-retrieving-an-individual-resource-get)
    * [Scenario: Creating a new resource (POST)](#scenario-creating-a-new-resource-post)
    * [Scenario: Modifying a resource (PUT)](#scenario-modifying-a-resource-put)
    * [Scenario: Deleting a resource (DELETE)](#scenario-deleting-a-resource-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Example Resource resource is ```osdi:example_resource``` for a single Example Resource resource or ```osdi:example_resources``` for a collection of Example Resource resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Answer Fields

An answer to a question.  An answer a user response to a question.

| Name          | Type      | Description
|-----------    |-----------|--------------
|identifier		|Identifier[]		|Array of identifiers
|value          |string     |Human readable text of the value

_[Back to top...](#)_



### Links

{% include links_intro.md %}

|Name          	|Type		|Description
|-----------    |-----------|--------------
|self			|Answer*	|A self-referential link to the resource.
|person		|Person*  |A link to a single Person resource representing the person to whom this Answer belongs.
|question		|Question*  |A link to the associated question

_[Back to top...](#)_




## Related Resources

* [Question](#)
* [Person](#)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of resources (GET)

Resource Example resources are sometimes presented as collections of resource example. For example, calling the resource example endpoint will return a collection of all the resource example stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/resource

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "total_pages": 88,
    "per_page": 25,
    "page": 1,
    "total_records": 2188,
    "_links": {
        "next": {
            "href": "https://osdi-sample-system.org/api/v1/resource?page=2"
        },
        "curies": [
            {
                "name": "osdi",
                "href": "https://osdi-sample-system.org/docs/v1/{rel}",
                "templated": true
            }
        ],
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/resource"
        }
    },
    "_embedded": {
        "osdi:resource": [
            //fields go here
        ]
    }
}
```

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual resource (GET)

Calling an individual Resource Example resource will return the resource directly, along with all associated fields and appropriate links to additional information about the resource.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/answer/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "value": "Strong Supporter"
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/resource/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
         "osdi:question": {
            "href": "https://osdi-sample-system.org/api/v1/question/asd3ds-7366-466d-a3b8-7e0d87c3cd8b"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/asd3ds-3234-466d-a3b8-4e0d87c323ds
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new resource (POST)

Posting to the resource collection endpoint will allow you to create a new resource. The response is the new resource that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/person/abc-123/questions/321-xyz

Header:
OSDI-API-Token:[your api key here]

{
    "value": "Strong Supporter"
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
    "value": "Strong Supporter"
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/resource/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
         "osdi:question": {
            "href": "https://osdi-sample-system.org/api/v1/question/asd3ds-7366-466d-a3b8-7e0d87c3cd8b
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/asd3ds-3234-466d-a3b8-4e0d87c323ds
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a resource (PUT)

You can updating a resource by calling a PUT operation on that resource's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/answers/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    // fields here
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
    ],
    // more fields/links here
}
```

_[Back to top...](#)_


### Scenario: Deleting a resource (DELETE)

You may delete a resource by calling the DELETE command on the resource's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/answers/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This resource was successfully deleted."
}
```

_[Back to top...](#)_
