---
layout: default
title: Status
---

{% include experimental.html %}

# Errors

OSDI reports response codes and errors according to a standard schema.  A combination of HTTP response codes and error objects is used to communicate the success or failure of a request.

### Sections:


* [Background](#background)
	* [Atomic vs Non-Atomic Requests](#atomic-vs-non-atomic-requests)
	* [Response Codes for Atomic Requests](#response-codes-for-atomic-requests)
* [Error Fields](#error-fields)
* [Related Objects](#related-objects)
	* [Resource Status](#resource-status)
	* [Error Description](#error-description)
* [Scenarios](#scenarios)
	* [Atomic Request](#atomic-request)
	* [Non-Atomic Request](#non-atomic-request)

_[Back to top...](#)_

The link relation label for an Error resource is ```osdi:error``` for a single Error resource.

## Background

### Atomic vs Non-Atomic Requests

While most OSDI requests are atomic (i.e., the request either succeeds completely, possibly changing the state of the system, or fails completely, leaving system unchanged), it is possible to create non-atomic requests using helpers.

For example, the [Person Signup Helper](person_signup.html) allows consumers to create a [Person](people.html) and a [Tagging](taggings.html) for the person in a single request.  However, if the Person  resource is valid but the Tagging is not, the Person may be created but the Tagging may not be created.

The ````osdi:error```` object for both types of requests is identical, except that atomic requests include only a single ````resource_status```` object, and non-atomic requests include multiple ````resource_status```` objects.  For non-atomic requests, if some resource(s) were created or updated as part of the request, the server may add these resources to the response, alongside the ````osdi:error```` resource.

_[Back to top...](#)_


### Response Codes for Atomic Requests

The following response codes correspond to success or failure of different kinds of atomic requests.  Response codes may be provided in the body of the response using the ````response_code```` field, unless forbidden by the HTTP spec (e.g., if the response code is 204).

| Type of request | Example | Description of result | Response Response Code | Response Body
|---------------- |-------- |---------------------- |--------- |----
| Any             | n/a     | Unexpected server error | 500 | [ErrorDescription](#error-description) indicating unexpected error; reference_code is recommended
| Any             | n/a     | Request not supported | 500 | [ErrorDescription](#error-description) indicating not-implemented
| Any             | n/a     | API key not valid | 401 | n/a
| Any             | n/a     | API key not allowed to execute this method | 403 | n/a
| Read collection of resources | GET  https://osdi-sample-system.org/api/v1/questions/ | At least one resource found | 200 | Representation of list of resources found
| Read collection of resources | GET  https://osdi-sample-system.org/api/v1/questions/ | No resources found | 200 | Either HAL empty collection document or empty JSON element {}
| Read single resource or subresource of single resource | GET  https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa | Resource found | 200 | Representation of resource found
| Read single resource or subresource of single resource | GET  https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa | Resource not found | 404 | n/a
| Create single resource | POST https://osdi-sample-system.org/api/v1/questions/ | Resource in request is not valid | 400 | [ErrorDescription[]](#error-description)
| Create single resource | POST https://osdi-sample-system.org/api/v1/questions/ | Resource in request is valid and was created | 201 | Representation of created resource
| Update single resource | PUT https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa | Resource in request is not valid | 400 | [ErrorDescription[]](#error-description)
| Update single resource | PUT https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa | Resource in request is valid and was updated | 200 | Representation of updated resource
| Delete single resource | DELETE https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa | Resource not found | 404 | [ErrorDescription[]](#error-description)
| Delete single resource | DELETE https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa | Resource found and deleted | 204 | n/a

_[Back to top...](#)_

## Error Fields

A list of fields specific to the Error resource.

|Name          |Type      |Description
|-----------    |-----------|--------------
|request_type   |enum       | One of "atomic", "non-atomic"
|response_code  |int        | An indication of the success or failure of the request as a whole.  Atomic requests should provide the appropriate value from the [Response Codes for Atomic Requests](#response-codes-for-atomic-requests) table.  Non-atomic requests should provide a value of 400.
|resource_status |[ResourceStatus[]](#resource-status) | An indication of the success or failure of each individual request.

_[Back to top...](#)_

### Related Objects

#### Resource Status

|Name          |Type      |Description
|-----------   |----------|--------------
|resource      |string    | The name of the OSDI resource involved in the request; for example "osdi:person".
|response_code      |int       | The success or failure of the request for the resource, as indicated in the  [Response Codes for Atomic Requests](#response-codes-for-atomic-requests) table.
|error_descriptions |[ErrorDescription[]](#error-description) | A description of the error(s) which caused the request for the resource to fail.

_[Back to top...](#)_

#### Error Description

| Name          | Type      | Description
|-----------    |-----------|--------------
| error_code			| string	| A machine-readable reason for the error: for example, ````START_DATE_AFTER_END_DATE````
| description	| string	| A human-readable reason for the error: for example, "The start date occurs after the end date."
| properties | string[] | An array of strings referencing the property or properties in the resource which cause the error; for example, ````['start_date', 'end_date']````.
| hint | string | An indication of how to resolve this error.  For example, if the property is an email address which is deemed invalid according to a regular expression, the regular expression can be provided here; e.g. ````.+@.+(\..+)+````
| reference_code | string | A string which refers to an internal error report which may be used to diagnose the problem; for example, "Logger-2015-03-10-cecc4e52-b350-4dac-87fc-39fc819f8c48"

_[Back to top...](#)_

# Scenarios

{% include scenarios_intro.md %}

## Atomic Request

The consumer sends a request, which is expected to succeed or fail atomically.

This request fails for two reasons. First, the implementing system does not allow multiple-choice responses for questions of type "Paragraph".  Second, because the implementing system uses a regular expression for validating the ````name```` property of question responses, but one of the question responses does not match that regular expression.  Both errors are reported.

### Request

````
POST https://osdi-sample-system.org/api/v1/questions/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "name": "Issues question",
    "title": "Which questions do you care about?",
    "description": "<p>Which issues do you care about? Select all that apply.</p>",
    "summary": "Issues the person cares about",
    "question_type": "Paragraph",
    "responses": [
      {
        "key": "hc",
        "name": "healthcare",
        "title": "Health care"
      },
      {
        "key": "env",
        "name": "environment",
        "title": "Environment"
      },
      {
        "key": "ec & jobs",
        "name": "economy",
        "title": "Economy and jobs"
      }
    ]
}
````

### Response

````
400 Bad Request

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "osdi:error": {
    "request_type": "atomic",
    "response_code": 400,
    "resource_status": [
       {
        "resource": "osdi:question",
        "response_code": 400,
        "error_descriptions": [
          {
            "error_code": "PARAGRAPH_CANNOT_HAVE_RESPONSES",
            "description": "A question of type 'Paragraph' may not have responses.",
            "properties": [ 'question_type', 'responses' ]
          },
          {
            "error_code": "RESPONSE_NAME_INVALID",
            "description": "The response name 'ec & jobs' is invalid.",
            "properties": [ 'responses[2].name' ],
            "hint": "^[A-Za-z0-9_]+$"
          }
        ]
       }
    ]
  }
}
````

_[Back to top...](#)_

## Non-Atomic Request

In this scenario, a consumer attempts to use the [Person Signup Helper](person_signup.html) to create a Person, add a Tagging to that person, and add the person to the List.  The Person object is valid, but the Tagging is invalid because the Tags in question do not exist.  Moreover the implementing system does not support the ````osdi:item```` resource, and therefore adding the person to the list fails, as well.  The Person is created but is not Tagged or added to a List.  The success of the Person creation, failure of the Tagging creation, and failure to add to a List are all reported.

Because the request as a whole is invalid, an Error with response code 400 is returned.

The server has also provided detail about the created Person via an ````osdi:person```` response.

### Request

````
POST https://osdi-sample-system.org/api/v1/people/person_signup_helper/

Header:
OSDI-API-Token:[your api key here]

{
    "person": {
        "identifiers": [
            "foreign_system:1"
        ],
        "family_name": "Edwin",
        "given_name": "Labadie",
        "additional_name": "Marques",
        "origin_system": "OpenSupporter",
        "email_addresses": [
            {
                "address":"test-3@example.com",
                "primary": true,
                "address_type": "Personal"
            }
        ],
        "postal_addresses": [
            {
                "primary": true,
                "address_lines": [
                    "935 Ed Lock"
                ],
                "locality": "New Dudley",
                "region": "MN",
                "postal_code": "17678",
                "country": "US",
                "address_type": "Home",
                "status": "Verified"
            }
        ],
        "phone_numbers": [
            {
                "primary": true,
                "number": 19876543210,
                "number_type": "Mobile",
                "sms_capable": true
            }
        ],
        "gender": "Male"
    },
    "add_tags": [
        "volunteer"
    ],
    "add_lists": [
        "supporters"
    ]
}
````

### Response

````
400 Bad Request

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "osdi:error": {
      "request_type": "non-atomic",
      "response_code": 400,
      "resource_status": [
        {
          "resource": "osdi:person",
          "response_code": 201
        },
        {
          "resource": "osdi:tagging",
          "response_code": 400,
          "errors": [
            {
              "code": "TAG_NAME_DOES_NOT_EXIST",
              "description": "The tag name 'volunteer' does not exist.",
              "properties": [ 'add_tags' ]
            },
          ]
        },
        {
          "resource": "osdi:item",
          "response_code": 500,
          "errors": [
            {
              "code": "NOT_SUPPORTED",
              "description": "The system does not support resources of this type."
            }
          ]
        }
      ]
   }
   "osdi:person": {
      "identifiers": [
          "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
          "foreign_system:1"
      ],
      "origin_system": "OSDI Sample System",
      "created_date": "2014-03-20T21:04:31Z",
      "modified_date": "2014-03-20T21:04:31Z",
      "given_name": "Labadie",
      "additional_name": "Marques",
      "family_name": "Edwin",
      "gender": "Male",
      "postal_addresses": [
          {
              "primary": true,
              "address_type": "Home",
              "address_lines": [
                  "935 Ed Lock"
              ],
              "locality": "New Dudley",
              "region": "MN",
              "postal_code": "17678",
              "country": "US",
              "language": "en",
              "location": {
                  "latitude": 38.919,
                  "longitude": -77.0379,
                  "accuracy": "Rooftop"
              }
              "status": "Verified"
          }
      ],
      "email_addresses": [
          {
              "primary": true,
              "address": "test-3@example.com",
              "address_type": "Personal"
          }
      ],
      "phone_numbers": [
          {
              "primary": true,
              "number": "19876543210",
              "number_type": "Mobile",
              "sms_capable": true,
          }
      ],
      "_links": {
          "self": {
              "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
          },
          "osdi:answers": {
              "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
          },
          "osdi:attendance": {
              "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendance"
          },
          "osdi:signatures": {
              "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/signatures"
          },
          "osdi:submissions": {
              "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions"
          },
          "osdi:donations": {
              "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
          },
          "osdi:taggings": {
              "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
          },
          "osdi:items": {
              "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/items"
          }
      }
   }
}
````

_[Back to top...](#)_

