---
layout: default
title: People Import Helper
---

# People Import Helper

This  document defines the People Import Helper resource.

The People import helper is a helper endpoint to aid in the import of a batch of [People](people.html) resources via POST. It provides a quick and easy way to add multiple people to an OSDI system.

The collection of people to be imported is represented in an array with the attribute name "signups".  Each element in the signups array is equivalent to the representation of a Person Signup Helper request.

Some systems may attempt to match inputs via the People import helper to existing people in the database and update their record instead of creating a new person for every POST. The method used for matching will be detailed in that system's documentation.

The response to a successful People import helper POST is an empty body, if there were no errors on any of the signups.

If errors occurred on individual signups, the response should contain an ````osdi:error```` object for batch requests indicating the individual status information.

### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [People import helper Fields](#people-import-helper-fields)
    * [Helper Action Functions](#helper-action-functions)
    * [Related Objects](#related-objects)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Importing People With Errors (POST)](#scenario-importing-people-with-errors-post)
    * [Scenario: Importing People Without Errors (POST)](#scenario-importing-people-without-errors-post)
    

{% include endpoints_and_url_structures.md %}

The link relation label for the People import helper is ```osdi:people_import_helper```.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

### People import helper Fields

A list of fields specific for POSTing via the People import helper.

|Name          |Type      |Description
|-----------    |-----------|--------------
|signups         |[PersonSignupHelper[]](person_signup.html) |An array of Person Signup Helper request representations.

{% include control_headers.md %}

### Import Response Fields

A list of fields for the response to People import helper.

|Name          |Type      |Description
|-----------    |-----------|--------------
|statistics     |object   | A vendor defined se
|submitted    | integer | A count of submitted records
|processed    | integer | A count of successfully processed records
|errors       | integer | A count of records which caused errors
|updated      | integer | A count of updated records
|created      | integer | A count of newly created records
|osdi:error   | OsdiError| OPTIONAL details of errors


_[Back to top...](#)_

### Helper Action Functions

{% include helper_action_functions.md %}

_[Back to top...](#)_

### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

#### Statistics

|Name          |Type      |Description
|-----------    |-----------|--------------


## Related Resources

* [Person](people.html)
* [PersonSignupHelper](person_signup.html)

_[Back to top...](#)_


## Scenarios

{% include scenarios_helper_intro.md %}


### Scenario: Importing People With Errors (POST)

Posting to the people import helper endpoint will allow you to upload a collection of people, as well as invoke helper action functions to add tags, lists, etc., for each person.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/people/people_import_helper

Header:
OSDI-API-Token:[your api key here]

{
    "signups": [
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
            },
{% include helper_action_examples_short.md prefix="            " %}
        },
        {
            "person": {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "given_name": "John",
                "family_name": "Smith",
                "honorific_prefix": "Mx.",
                "honorific_suffix": "Ph.D",
                "email_addresses": [
                    {
                        "primary": true,
                        "address": "johnsmith@mail.com",
                        "address_type": "Personal",
                        "status": "subscribed"
                    }
                ],
                "phone_numbers": [
                  {
                    "number": "1-800-OSDI-RULES",
                    "number_type": "Home"
                  }
                ]
            },
{% include helper_action_examples_short.md prefix="            " %}
        }
    ]
}
```

#### Response

````json
207 Multistatus

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "submitted": 2,
  "successful": 1,
  "errors": 1,
  "osdi:error": {
    "request_type": "batch",
    "response_code": 200,
    "batch_errors": [
      {
        "request_type": "non-atomic",
        "response_code": 207,
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
        ]
      },
      {
        "request_type": "non-atomic",
        "response_code": 400,
        "resource_status": [
          {
            "resource": "osdi:person",
            "response_code": 400,
            "errors": [
              {
                "code": "INVALID PHONE NUMBER",
                "description": "The phone number '1-800-OSDI-RULES' is not a valid phone number.",
                "properties": [ 'phone_numbers[0].number' ]
              },
            ]
          }
        ]
      }
    ]
  }
}
````

_[Back to top...](#)_


### Scenario: Importing People Without Errors (POST)

Posting to the people import helper endpoint will allow you to upload a collection of people, as well as invoke helper action functions to add tags, lists, etc., for each person.

#### Request

```json
POST https://osdi-sample-system.org/api/v1/people/people_import_helper

Header:
OSDI-API-Token:[your api key here]

{
    "signups": [
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
            },
{% include helper_action_examples_short.md prefix="            " %}
        },
        {
            "person": {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "given_name": "John",
                "family_name": "Smith",
                "honorific_prefix": "Mx.",
                "honorific_suffix": "Ph.D",
                "email_addresses": [
                    {
                        "primary": true,
                        "address": "johnsmith@mail.com",
                        "address_type": "Personal",
                        "status": "subscribed"
                    }
                ],
                "phone_numbers": [
                  {
                    "number": "1-800-OSDI-RULES",
                    "number_type": "Home"
                  }
                ]
            },
{% include helper_action_examples_short.md prefix="            " %}
        }
    ]
}
```

#### Response

````json
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "submitted": 2,
  "successful": 1,
  "errors": 1,
  "osdi:error": {
    "request_type": "batch",
    "response_code": 200,
    "batch_errors": [
      {
        "request_type": "non-atomic",
        "response_code": 207,
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
              }
            ]
          }
        ]
      },
      {
        "request_type": "non-atomic",
        "response_code": 400,
        "resource_status": [
          {
            "resource": "osdi:person",
            "response_code": 400,
            "errors": [
              {
                "code": "INVALID PHONE NUMBER",
                "description": "The phone number '1-800-OSDI-RULES' is not a valid phone number.",
                "properties": [ 'phone_numbers[0].number' ]
              }
            ]
          }
        ]
      }
    ]
  }
}
````

_[Back to top...](#)_
