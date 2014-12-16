---
layout: default
title: Resource Name
---

# Example Resource

Introductory paragraphs describing the resource. 

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Resource Fields](#resource-fields)
    * [Related Objects](#related-objects)   
    * [Links](#links)
* [Helpers](#helpers)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of resources (GET)](#scenario-retrieving-a-collection-of-resources-get)
    * [Scenario: Retrieving an individual resource (GET)](#scenario-scenario-retrieving-an-individual-resource-get)
    * [Scenario: Creating a new resource (POST)](#scenario-creating-a-new-resource-post)
    * [Scenario: Modifying a resource (PUT)](#scenario-modifying-a-resource-put)
    * [Scenario: Deleting a resource (DELETE)](#scenario-deleting-a-resource-delete)


{% include endpoints_and_url_structures.md %}


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_

### Resource-Specific Fields

A list of fields specific to the resource.

|Name          |Type      |Description
|-----------    |-----------|--------------
|field1      |string     |field1 description
|field2|[ExampleObject](#example-object)    |An instance of an Example Object
|field3      |[ExampleObject[]](#example-object)  |An array of Example Objects

_[Back to top...](#)_

### Related Objects

These objects included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

#### Example Object

|Name          |Type      |Description
|-----------    |-----------|--------------
|field1      |string       |Description of field1
|field2      |string       |Description of field2

_[Back to top...](#)_



### Links

{% include links_intro.md %}

|Name          	|Type		|Description
|-----------    |-----------|--------------
|linked_resource1		|LinkedResourceType1*  |A link to the instance of LinkedResourceType1
|linked_resource2		|LinkedResourceType2[]*  |A link to the collection of resources

_[Back to top...](#)_



## Helpers

{% include helpers_intro.md %}

|Name          |Description
|-----------    |-----------
|example_helper1      |Description of helper's purpose.
|example_helper2      |Description of helper's purpose.

_[Back to top...](#)_


## Related Resources

* [RelatedResource1](#)
* [RelatedResource2](#)

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of resources (GET)

Description of scenario

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
    //(truncated for brevity)
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
  }

```

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual resource (GET)

Description of how to get an individual resource

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/resource/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
  "_links": {
    "self": {
      "href": "https://osdi-sample-system.org/api/v1/resource/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
    }

	// truncated
}
```

_[Back to top...](#)_


### Scenario: Creating a new resource (POST)

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/resource/

Header:
OSDI-API-Token:[your api key here]

{
	// truncated
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
    // truncated
}
```

_[Back to top...](#)_


### Scenario: Modifying a resource (PUT)

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/resource/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    // truncated
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
    
	// truncated
}
```

_[Back to top...](#)_


### Scenario: Deleting a resource (DELETE)

You may delete a resource by calling the DELETE command on the resource's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/resource/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
