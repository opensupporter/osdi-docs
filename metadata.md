---
layout: default
title: Metadata
---

# Metadata

This page defines the Metadata Endpoint.

Metadata endpoint is a collection of resources that can be queried to gather information needed to work with OSDI resources. For instance, to record [Canvass[]](#canvasses) responses precisely, it is essential for the client to get the available options for canvass fields (ex: status codes or contact types). Collection of canvass fields supported by the system can be obtained by querying the resources available under the metadata endpoint.

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving the collection of resources under metadata endpoint (GET)](#scenario-retrieving-the-collection-of-resources-under-metadata-endpoint-get)
    * [Scenario: Retrieving the collection of canvass response codes (GET)](#scenario-retrieving-the-collection-of-canvass-response-codes-get)
    * [Scenario: Retrieving the collection of canvass contact types (GET)](#scenario-retrieving-the-collection-of-canvass-contact-types-get)
    * [Scenario: Retrieving the collection of canvass input types (GET)](#scenario-retrieving-the-collection-of-canvass-input-types-get)



{% include endpoints_and_url_structures.md %}


The link relation label for Metadata endpoint is ```osdi:metadata``` and the link relation label for metadata resources 
will be under ```osdi:<metadata_url>```, for instance ```osdi:canvass_response_codes``` has list of canvass status codes supported by the system. 

_[Back to top...](#)_


## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving the collection of resources under metadata endpoint (GET)

Metadata endpoint is presented as collections of resources. For example, calling the metadata endpoint will return a collection of resources that the system supports.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/metadata

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "name": "NGP VAN OSDI Metadata",
  "_links": {
    "curies": [
      {
        "name": "osdi",
        "href": "https://osdi-sample-system.org/docs/v1/{rel}",
        "templated": true
      }
    ],
    "self": {
      "href": "https://osdi-sample-system.org/api/v1/metadata",
      "title": "NGP VAN OSDI Metadata"
    },
    "osdi:canvass_response_codes": {
      "href": "https://osdi-sample-system.org/api/v1/metadata/canvass_response_codes",
      "title": "The collection of canvass response codes in the system"
    },
    "osdi:canvass_contact_types": {
      "href": "https://osdi-sample-system.org/api/v1/metadata/canvass_contact_types",
      "title": "The collection of canvass contact types in the system"
    },
    "osdi:canvass_input_types": {
      "href": "https://osdi-sample-system.org/api/v1/metadata/canvass_input_types",
      "title": "The collection of canvass input types in the system"
    }
  }
}
```
_[Back to top...](#)_


### Scenario: Retrieving the collection of canvass response codes (GET)

This resource is a collection of canvass response codes supported by the system.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/metadata/canvass_response_codes

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "origin_system": "VAN",
    "name": "Available response codes",
    "description": "Available response codes",
    "identifiers": [
        "VAN:ResultCodes"
    ],
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/metadata/canvass_response_codes"
        },
        "curies": [
            {
                "name": "osdi",
                "href": "http://osdi-sample-system.org/osdi#{rel}",
                "templated": true
            }
        ]
    },
    "response_codes": [
        {
            "response_code": 59,
            "name": "Bounced"
        },
        {
            "response_code": 18,
            "name": "Busy"
        },
        {
            "response_code": 17,
            "name": "Call Back"
        },
    ]
}

```	

_[Back to top...](#)_


### Scenario: Retrieving the collection of canvass contact types (GET)

This resource is a collection of canvass contact types supported by the system.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/metadata/canvass_contact_types

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "origin_system": "VAN",
    "name": "Available contact types",
    "description": "Available contact types",
    "identifiers": [
        "VAN:ContactTypes"
    ],
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/metadata/canvass_contact_types"
        },
        "curies": [
            {
                "name": "osdi",
                "href": "http://osdi-sample-system.org/osdi#{rel}",
                "templated": true
            }
        ]
    },
    "contact_types": [
        {
            "contact_type": 1,
            "name": "Phone"
        },
        {
            "contact_type": 2,
            "name": "Walk"
        },
    ]
}

``` 

_[Back to top...](#)_


### Scenario: Retrieving the collection of canvass input types (GET)

This resource is a collection of canvass input types supported by the system.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/metadata/canvass_input_types

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "origin_system": "VAN",
    "name": "Available input types",
    "description": "Available input types",
    "identifiers": [
        "VAN:InputTypes"
    ],
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/metadata/canvass_input_types"
        },
        "curies": [
            {
                "name": "osdi",
                "href": "http://osdi-sample-system.org/osdi#{rel}",
                "templated": true
            }
        ]
    },
    "input_types": [
        {
            "input_type": 11,
            "name": "API"
        },
        {
            "input_type": 4,
            "name": "Bulk"
        },
        {
            "input_type": 2,
            "name": "Manual"
        },
    ]
}

``` 

_[Back to top...](#)_