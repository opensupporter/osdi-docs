---
layout: default
title: Status Codes and Errors
---

# Status Codes and Errors

OSDI reports errors and status information according to a standard schema.  A combination of HTTP status codes and error objects is used to communicate the success or failure of a request.

### Sections:

* [Status Codes](#status-codes)
* [Errors](#errors)
* [Non-atomic requests](#non-atomic-requests)
* [Scenarios](#scenarios)
    * [Scenario: Attempt to create invalid resource atomically](#attempt-to-create-invalid-resource-atomically)
    * [Scenario: Invalid non-atomic request](#invalid-non-atomic-request)

## Status Codes

The following status codes correspond to success or failure of different kinds of requests.  Status codes may be provided in the body of the response using the ````osdi:status```` resource, unless forbidden by the HTTP spec (e.g., if the response code is 204).

| Type of request | Example | Description of result | Response Status Code | Response Body
|---------------- |-------- |---------------------- |--------- |----
| Any             | n/a     | Unexpected server error | 500 | n/a
| Any             | n/a     | Request not supported | 405 | n/a
| Any             | n/a     | API key not valid | 401 | n/a
| Any             | n/a     | API key not allowed to execute this method | 403 | n/a
| Read multiple resources | GET  https://osdi-sample-system.org/api/v1/questions/ | At least one resource found | 200 | Representation of list of resources found
| Read multiple resources | GET  https://osdi-sample-system.org/api/v1/questions/ | No resources found | 404 | n/a
| Read single resource | GET  https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa | Resource found | 200 | Representation of resource found
| Read single resource | GET  https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa | Resource not found | 404 | n/a
| Create single resource | POST https://osdi-sample-system.org/api/v1/questions/ | Resource in request is not valid | 400 | [Error*](#errors)
| Create single resource | POST https://osdi-sample-system.org/api/v1/questions/ | Resource in request is valid and was created | 201 | Representation of created resource
| Update single resource | PUT https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa | Resource in request is not valid | 400 | [Error*](#errors)
| Update single resource | PUT https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa | Resource in request is valid and was updated | 200 | Representation of updated resource
| Delete single resource | DELETE https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa | Resource not found | 404 | [Error*](#errors)
| Delete single resource | DELETE https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa | Resource found and deleted | 204 | n/a


## Errors

When a request includes an invalid resource which cannot be created or updated, the implementing system should report the reason that the resource is invlid as a list of errors.  Each error should have the following fields.  While code and description are required, the other properties are optional.  Errors are provided via the "osdi:errors" resource.

| Name          | Type      | Description
|-----------    |-----------|--------------
| code			| string	| A machine-readable reason for the error: for example, ````START_DATE_AFTER_END_DATE````
| description	| string	| A human-readable reason for the error: for example, "The start date occurs after the end date."
| properties | string[] | An array of strings referencing the property or properties in the resource which cause the error; for example, ````['start_date', 'end_date']````.
| hint | string | An indication of how to resolve this error.  For example, if the property is an email address which is deemed invalid according to a regular expression, the regular expression can be provided here; e.g. ````.+@.+(\..+)+````
| reference_code | string | A string which refers to an internal error report which may be used to diagnose the problem; for example, "Logger-2015-03-10-cecc4e52-b350-4dac-87fc-39fc819f8c48"

## Non-atomic requests

While most OSDI requests are atomic (i.e., the request either succeeds completely, possibly changing the state of the system, or fails completely, leaving system unchanged), it is possible to create non-atomic requests using helpers.

For example, the [Person Signup Helper](person_signup.html) allows consumers to create a [Person](people.html) and a [Tagging](taggings.html) for the person in a single request.  However, if the Person  resource is valid but the Tagging is not, the Person may be created but the Tagging may not be created.  In this case the system should report back that the Person has been created while the Tagging has failed, and why it failed, using the ````osdi:resource```` resource in conjunction with ````osdi:status```` and ````osdi:errors```` in order to report status or failure for the individual resources.

# Scenarios

## Attempt to create invalid resource atomically

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
  "osdi:status": 400,
  "osdi:errors": [
    {
      "code": "PARAGRAPH_CANNOT_HAVE_RESPONSES",
      "description": "A question of type 'Paragraph' may not have responses.",
      "properties": [ 'question_type', 'responses' ]
    },
    {
      "code": "RESPONSE_NAME_INVALID",
      "description": "The response name 'ec & jobs' is invalid.",
      "properties": [ 'responses[2].name' ],
      "hint": "^[A-Za-z0-9_]+$"
    }
  ]
}
````


## Invalid non-atomic request

In this scenario, a consumer attempts to use the [Person Signup Helper](person_signup.html) to create a Person, add a Tagging to that person, and add the person to the List.  The Person object is valid, but the Tagging is invalid because the Tags in question do not exist.  The success of the Person creation, failure of the Tagging creation, and addition to the List are all reported.

Because the request as a whole is invalid, a 400 is returned.

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
                "country": "RU",
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
        "volunteer",
        "donor"
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

[
  {
    "osdi:resource": "osdi:person",
    "osdi:status": 201
  },
  {
    "osdi:resource": "osdi:tagging",
    "osdi:status": 400,
    "osdi:errors": [
      {
        "code": "TAG_NAME_DOES_NOT_EXIST",
        "description": "The tag name 'volunteer' does not exist.",
        "properties": [ 'add_tags' ]
      }
    ]
  },
  {
    "osdi:resource": "osdi:item",
    "osdi:status": 201
  }
]
````
